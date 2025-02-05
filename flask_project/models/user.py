from db import db 

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(60), nullable= False, unique = True)
    password = db.Column(db.String(50), nullable = False)
    
