from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required = True)
    shop_id = fields.Str(required=True)
    brand = fields.Str(required=False)

class ProductUpdateSchema(Schema):
    name = fields.Str()
    price= fields.Float()

class ShopProductSchema(Schema):
    prod_name = fields.Str(required=True)
    price = fields.Float(required=True)
    brand = fields.Str(required=False)

class ShopSchema(Schema):
    id = fields.Str(dump_only=True) 
    shop_name = fields.Str(required=True)
    product = fields.List(fields.Nested(ShopProductSchema))


