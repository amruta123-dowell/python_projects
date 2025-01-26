from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import shops
from schemas import ShopSchema
import uuid
blueprint = Blueprint("shops", __name__, description = "Operations in shop")
@blueprint.route("/shop")
class ShopList(MethodView):
    @blueprint.response(200, ShopSchema(many=True))
    def get(self):
        return list(shops.values())
    
    @blueprint.arguments(ShopSchema)
    @blueprint.response(200,ShopSchema)
    def post(self,shop_data):
        print("Shop post is called")
        for data in shops.values():
            if(shop_data["shop_name"] == data["shop_name"]):
                print("The name is exist")
                abort(400, message = "The shop name is already exist")
        shop_id = uuid.uuid4().hex
        shop_details = {**shop_data, "id":shop_id}
        shops[shop_id] = shop_details
        return shops[shop_id]
        

@blueprint.route("/shop/<shop_id>")
class Shop(MethodView):
    @blueprint.response(200, ShopSchema)
    def get(self,shop_id):
        try:
            return shops[shop_id]
        except KeyError:
            abort(404, message = "Shop not found")
            
    def delete(self, shop_id):
        try:
            del(shops[shop_id])
            return {"message":"Shop is deleted successfully"}
        except KeyError:
            abort(404, message = "Shop is not found")