from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'

db=SQLAlchemy(app)
migrate=Migrate(app, db)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=True)
    email=db.Column(db.String(200),nullable=True)
    fullname=db.Column(db.String(200), nullable=True)

if __name__== '__main__':
    app.run(debug=True, port=5001)