from flask import Flask, request
from flask.views import MethodView
import uuid
from db import db
from flask_smorest import Blueprint, abort
from schemas import ProductSchema, ProductUpdateSchema
from models.product import ProductModel

from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_jwt_extended import JWTManager, jwt_required

blueprint = Blueprint('products', __name__, description = 'Operations in shop')

@blueprint.route('/product')
class ProductList(MethodView):
    # get product
    @jwt_required(fresh=True)
    @blueprint.response(200, ProductSchema(many=True))
    def get(self):
        # To get the list data from the database
        return  ProductModel.query.all()
        # return list(products.values())
    
    # add product
    @jwt_required(fresh=True)
    @blueprint.arguments(ProductSchema)
    @blueprint.response(201,ProductSchema)
    def post(self, product_data):
        product_model = ProductModel(**product_data)
         

        try:
             db.session.add(product_model)
             db.session.commit()
        except IntegrityError:
            abort(400, message = "A product with name is already exist")     
        except SQLAlchemyError:
            abort(500, message ='An occurred while inserting the product')
    
        return product_model



@blueprint.route('/product/<product_id>')
class Product(MethodView):
    @jwt_required(fresh=True)
    @blueprint.response(200, ProductSchema(many=True))
    def get(self,product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product
      
    @jwt_required(fresh=True)
    @blueprint.arguments(ProductUpdateSchema) 
    @blueprint.response(200, ProductSchema)
    def put(self, product_data,product_id):
           product = ProductModel.query.get_or_404(product_id)
           if product:
               product.name = product_data.get("name", product.name)
               product.price = product_data.get("price", product.price)
           else:
               product = ProductModel(id = product_id, **product_data)

           try:
               db.session.add(product)
               db.session.commit()

           except SQLAlchemyError:
               abort(400, message ='Error while updating the Product' )

           return product


   
    @jwt_required(fresh=True)
    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message":"The product is deleted successfully"}
