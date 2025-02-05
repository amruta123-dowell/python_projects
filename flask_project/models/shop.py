

from db import db
class ShopModel(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), nullable=False, unique= True)
    products = db.relationship('ProductModel', back_populates ='shop', lazy = 'dynamic', cascade = 'all, delete')


# use of cascade
# cascade = 'all, delete' means that when a shop is deleted, all its products will also be deleted.
                               
