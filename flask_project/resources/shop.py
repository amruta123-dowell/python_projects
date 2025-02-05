from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from db import db
from schemas import ShopSchema
import uuid
from models.shop import ShopModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
blueprint = Blueprint("shops", __name__, description = "Operations in shop")
@blueprint.route("/shop")
class ShopList(MethodView):
    @jwt_required()
    @blueprint.response(200, ShopSchema(many=True))
    def get(self):
        return ShopModel.query.all()
    # list(shops.values())
    @jwt_required()
    @blueprint.arguments(ShopSchema)
    @blueprint.response(200,ShopSchema)
    def post(self,shop_data):
        print("Shop post is called")
        shop = ShopModel(**shop_data)
        try:
            # creating entry in the database
            db.session.add(shop)
            db.session.commit()
            # To handle the exception of the shop name already exist
        except IntegrityError:
            db.session.rollback() 
            abort(400, message = "The shop name is already exist")
        
        except SQLAlchemyError:
            abort(500, message = "An error occurred while inserting the shop")
        return shop

        # for data in shops.values():
        #     if(shop_data["shop_name"] == data["shop_name"]):
        #         print("The name is exist")
        #         abort(400, message = "The shop name is already exist")
        # shop_id = uuid.uuid4().hex
        # shop_details = {**shop_data, "id":shop_id}
        # shops[shop_id] = shop_details
        # return shops[shop_id]
        

@blueprint.route("/shop/<shop_id>")
class Shop(MethodView):
    @jwt_required()
    @blueprint.response(200, ShopSchema)
    def get(self,shop_id):
        shop = ShopModel.query.get_or_404(shop_id); 
        return shop
    
        # try:
        #     return shops[shop_id]
        # except KeyError:
        #     abort(404, message = "Shop not found")
    @jwt_required()        
    def delete(self, shop_id):
        shop = ShopModel.query.get_or_404(shop_id)
        db.session.delete(shop)
        db.session.commit()
        return {"message":"Deleted Successfully"}

    

        # try:
        #     del(shops[shop_id])
        #     return {"message":"Shop is deleted successfully"}
        # except KeyError:
        #     abort(404, message = "Shop is not found")