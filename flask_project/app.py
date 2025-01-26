from flask import Flask,  request

from flask_smorest import Api
from resources.shop import blueprint as ShopBluePrint
from resources.product import blueprint as ProductBluePrint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# to run the App

api = Api(app)
api.register_blueprint(ShopBluePrint)
api.register_blueprint(ProductBluePrint)
# app.run()

if __name__ == "__main__":
    app.run(debug=True)

