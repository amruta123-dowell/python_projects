from marshmallow import Schema, fields

# class ProductSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)
#     price = fields.Float(required = True)
#     shop_id = fields.Str(required=True)
#     brand = fields.Str(required=False)

# class ProductUpdateSchema(Schema):
#     name = fields.Str()
#     price= fields.Float()

# class ShopProductSchema(Schema):
#     prod_name = fields.Str(required=True)
#     price = fields.Float(required=True)
#     brand = fields.Str(required=False)

# class ShopSchema(Schema):
#     id = fields.Str(dump_only=True) 
#     shop_name = fields.Str(required=True)
#     product = fields.List(fields.Nested(ShopProductSchema))



class PlainProductSchema(Schema):
    name= fields.Str(required = True)
    price = fields.Float(required=True)
    brand = fields.Str(required=False)

class PlainShopSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str(required=True)

class ProductSchema(PlainProductSchema):
    id = fields.Int(dump_only = True)
    shop_id= fields.Int(required = True)
    shop= fields.Nested(PlainShopSchema(), dump_only = True)


class ShopSchema(PlainShopSchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only = True)

class ProductUpdateSchema(Schema):
    name = fields.Str(required= False)
    price = fields.Float(required = True)


class UserModelSchema(Schema):
    id = fields.Int(dump_only = True)
    username = fields.Str(required=True)
    password = fields.Str(required= True)




