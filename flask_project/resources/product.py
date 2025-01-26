from flask import Flask, request
from flask.views import MethodView
import uuid
from db import products
from flask_smorest import Blueprint, abort
from schemas import ProductSchema, ProductUpdateSchema
from flask_


blueprint = Blueprint("products", __name__, description = "Operations in shop")

@blueprint.route("/product")
class ProductList(MethodView):
    # get product
    @blueprint.response(200, ProductSchema(many=True))
    def get(self):
        return list(products.values())
    
    # add product
    @blueprint.arguments(ProductSchema)
    @blueprint.response(200,ProductSchema)
    def post(self, product_data):
        print(product_data)
        print("Product is called")
        for data in products:
            if(data["prod_name"] == product_data["prod_name"]):
                abort(404, message = "Product is already exist")
        prod_id = uuid.uuid4().hex
        products[prod_id] = {**product_data, "id":prod_id}
        return products[prod_id]


@blueprint.route("/product/<product_id>")
class Product(MethodView):
    @blueprint.response(200, ProductSchema(many=True))
    def get(self,product_id):
        try:

            return products[product_id]
        except:
            abort(404, {"message":"The product is not found"})

    @blueprint.arguments(ProductUpdateSchema) 
    @blueprint.response(200, ProductSchema)
    def put(self, product_data,product_id):
         
        try:
            products[product_id]|= product_data
            return products[product_id]
        except KeyError:
            abort(404, {"message":"Product is not found"})

   
    
    def delete(self, product_id):
        try:
            del(products[product_id])
            return {"message":"Product  is deleted successfully"}
        except KeyError:
            abort(404, message = "Product  is not found")
  
    # def get(self, product_id):
    #     try:
    #         return list(products[product_id])
    #     except:
    #         abort(400, {"message":"Product name is not found"})