#class Post:
#	def __init__(self, title, author, content): #the initialization method
#		self.title = title  		#defining the title attribute
#		self.author = author 		#defining the author attribute 
#		self.content = content		#defining the conten attribute

from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname= db.Column(db.String(64))
	lastname= db.Column(db.String(64))
	username= db.Column(db.String(120), unique= True)
	posts = db.relationship('Post', backref = 'author')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title=db.Column(db.String(100))
	content=db.Column(db.Text)
	author_id=db.Column(db.Integer, db.ForeignKey('user.id'))

#remember the _id note on author for the post because it is an integer and you want o remember that 
#the lowercase 'user.id' refers to the uppercase User function at the very top 




