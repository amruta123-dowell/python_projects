from flask_smorest import Blueprint, abort
from flask.views import MethodView
from db import db
from models import UserModel
from schemas import UserModelSchema
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required

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
    @jwt_required()
    @blueprint.response(200,UserModelSchema(many=True))
    def get(self):
        return UserModel.query.all()


@blueprint.route("/login")
class UserLogin(MethodView):
    @blueprint.arguments(UserModelSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username== user_data["username"]).first()
        if(user and pbkdf2_sha256.verify( user_data["password"], user.password)):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 201
        
        abort(401, message = "Invalid credentials")
