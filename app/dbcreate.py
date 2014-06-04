#dbcreate.py

#create the database on the models we've defined in models.py

#this is a general template that you can use again and again and again 
from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all()