from flask import Flask,  request,jsonify

from flask_smorest import Api
from db import db
from resources.shop import blueprint as ShopBluePrint
from resources.product import blueprint as ProductBluePrint
from resources.user import blueprint as UserBluePrint
import os
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Set default database URI if environment variable is missing
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")

# Other configuration
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["JWT_SECRET_KEY"] = "amruta_dowell"


jwt = JWTManager()
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return (jsonify({"message":'The provided token is expired', "error":"Token_expired"}), 401)

@jwt.invalid_token_loader
def invalid_token_loader_callback(error):
    return (jsonify({"message":"Signature verification failed", 
                     "error":"Invalid token"}),
                       401)
@jwt.unauthorized_loader
def unauthorized_loader_callback(error):
    return (jsonify({"message":"Request doesn't contain an access token", 
                     "error":"authorization required"
                     }), 401)


# To register the db 
db.init_app(app)
# to run the App

api = Api(app)

api.register_blueprint(ShopBluePrint)
api.register_blueprint(ProductBluePrint)
api.register_blueprint(UserBluePrint)
# app.run()
# Create database tables before running
with app.app_context():
    db.create_all()  # Ensure tables are created
if __name__ == "__main__":
    app.run(debug=True, use_reloader= False)

