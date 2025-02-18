from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models import UserModel
from schemas import UserModelSchema
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (create_access_token,
                                jwt_required, get_jwt, 
                                create_refresh_token,
                                 get_jwt_identity)
from blacklist import BLACKLIST
from datetime import timedelta
blueprint = Blueprint("Users", "users", description = "Operations in Users")

@blueprint.route("/register")
class UserRegister(MethodView):
    @blueprint.arguments(UserModelSchema)
    def post(self, user_data):
        if(UserModel.query.filter(UserModel.username== user_data["username"]).first()):
            abort(409, message = "A provided user name already exist")
        user = UserModel(username= user_data["username"], password = pbkdf2_sha256.hash(user_data["password"]))

        db.session.add(user)
        db.session.commit()
        return {"message":"User is created", }, 201
    


   
@blueprint.route("/user")
class User(MethodView):
    @jwt_required(fresh=True)
    @blueprint.response(200,UserModelSchema(many=True))
    def get(self):
        return UserModel.query.all()


@blueprint.route("/login")
class UserLogin(MethodView):
    @blueprint.arguments(UserModelSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()
        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id) ,fresh=True, expires_delta=timedelta(minutes=10))
            refresh_token = create_refresh_token(str(user.id))
            print(f"ACCESS TOKEN: {access_token}")  # Debugging
            return {"access_token": access_token, "Refresh_token": refresh_token}, 201
        
        abort(401, message="Invalid credentials")


@blueprint.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def delete(self):
        jti = get_jwt()["jti"]
        BLACKLIST.add(jti)
        return {"message":"Successfully deleted"}, 200

@blueprint.route("/refresh")
class TokenRefresh(MethodView):
    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)
        jti= get_jwt()["jti"]
        BLACKLIST.add(jti)
        return { "access_token":new_token },200
   
