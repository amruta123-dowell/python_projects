from flask import Flask, jsonify, request
app = Flask(__name__)

shopdata= [{"shop_name":"AmrutaGrocery", "product":[{"prod_name":"pencil", "price":10, "brand":"Nataraj"}]}]

@app.route("/shops")
def getShops():
    
    return shopdata
    # return "Learn python flask framework"


# post method - create shop
@app.route("/addShopDetails", methods=['POST'])
def createShop():
    shop = request.json
    shopdata.append(shop)
    return "success", 201

#add product in particular shop - POST method
@app.route("/shops/<shop_name>/add_product", methods = ["POST"])
def createProduct(shop_name):
    new_prod =request.json
    for data in shopdata:
        if(data["shop_name"]==shop_name):
            data["product"].append(new_prod)
            return new_prod, 201
    return {"message":"Shop name is not found"}, 404

@app.route("/shops/<shop_name>", methods=["GET"])

def getIndividualDetails(shop_name):
    for data in shopdata:
        if(data["shop_name"]==shop_name):
            return data, 201
    return {"message":"Shop details are not found"}, 404

if __name__== "__main__":
    app.run()