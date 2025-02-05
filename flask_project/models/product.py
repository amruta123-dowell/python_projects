from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
# from models.shop import ShopModel


# class ShopModel(db.Model):
#     __tablename__ = 'shops'
#     id = db.Column(db.Integer, primary_key= True)
#     name = db.Column(db.String(100), nullable=False)
#     products = db.relationship('ProductModel', back_populates ='shop', lazy = 'dynamic', cascade = 'all, delete')

class ProductModel(db.Model):
    __tablename__ ="products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique = True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=True)
    shop_id =db.Column(db.Integer, db.ForeignKey("shops.id"), nullable=False, unique= False)
    shop = db.relationship("ShopModel",back_populates="products")

