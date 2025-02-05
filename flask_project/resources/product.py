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
    @jwt_required()
    @blueprint.response(200, ProductSchema(many=True))
    def get(self):
        # To get the list data from the database
        return  ProductModel.query.all()
        # return list(products.values())
    
    # add product
    @jwt_required()
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



        # print(product_data)
        # print('Product is called')
        # for data in products:
        #     if(data['prod_name'] == product_data['prod_name']):
        #         abort(404, message = 'Product is already exist')
        # prod_id = uuid.uuid4().hex
        # products[prod_id] = {**product_data, 'id':prod_id}
        # return products[prod_id]


@blueprint.route('/product/<product_id>')
class Product(MethodView):
    @jwt_required()
    @blueprint.response(200, ProductSchema(many=True))
    def get(self,product_id):
        product = ProductModel.query.get_or_404(product_id)
        return product
        # try:

        #     return products[product_id]
        # except:
        #     abort(404, {'message':'The product is not found'})
    @jwt_required()
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
               
        # try:
         
           
        #     # products[product_id]|= product_data
        #     # return products[product_id]
        # except KeyError:
        #     abort(404, {'message':'Product is not found'})

   
    @jwt_required()
    def delete(self, product_id):
        product = ProductModel.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        return {"message":"The product is deleted successfully"}
        # try:
        #     del(products[product_id])
        #     return {'message':'Product  is deleted successfully'}
        # except KeyError:
        #     abort(404, message = 'Product  is not found')
  
    # def get(self, product_id):
    #     try:
    #         return list(products[product_id])
    #     except:
    #         abort(400, {'message':'Product name is not found'})