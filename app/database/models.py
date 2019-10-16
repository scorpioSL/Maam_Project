# #################################################################################################
# Flask Server Imports
from flask import Flask
from flask_login import UserMixin
# MongoEngine Imports
import mongoengine as db
# #################################################################################################
import datetime

db.connect('MaamDB', alias='default')

class User(UserMixin,db.Document):
	UserPassword=db.StringField()
	UserName=db.StringField()
	UserType=db.ReferenceField('UserType')
	UserAccess=db.BooleanField(defaul=False)
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class UserType(db.Document):
	TypeDescription=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class UserLog(db.Document):
	User=db.StringField()
	Action = db.StringField()
	Description=db.StringField()
	Response=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	


class Post(db.Document):
	PostTittle=db.StringField()
	PostSubTitle = db.StringField()
	PostContent=db.StringField()
	PostImage=db.StringField()
	PostType=db.ReferenceField('PostType')
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class PostType(db.Document):
	PostTypeDescription=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class Vacancy(db.Document):
	Tittle=db.StringField()
	DepartmentId=db.ReferenceField('Department')
	Poster=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class Department(db.Document):
	DepDescription=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	
class Feedback(db.Document):
	Name=db.StringField()
	TelNumber=db.StringField()
	Country=db.StringField()
	Email=db.StringField()
	Message=db.StringField()
	FeedbackTypeId=db.ReferenceField('FeedbackType')
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class FeedbackType(db.Document):
	Description=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()

class Applicant(db.Document):
	ApplicantName=db.StringField()
	ApplicantFullname=db.StringField()
	ApplicantAddress=db.StringField()
	ApplicantAcadamicQuali=db.StringField()
	ApplicantOtherQuali=db.StringField()
	ApplicantExperience=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class Distributor(db.Document):
	InvestmentAmount=db.StringField()
	Item=db.StringField()
	ItemQuantity=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class Supplier(db.Document):
	SupplierName=db.StringField()
	SupplierAddress=db.StringField()
	SupplierLeadTime=db.StringField()
	SupplierNic=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	
class FinishedGood(db.Document):
	ItemCode=db.StringField()
	ItemName=db.StringField()
	ItemUnit=db.StringField()
	ItemPrice=db.StringField()
	CatId=db.ReferenceField('FinishedGoodCategory')
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	

class FinishedGoodCategory(db.Document):
	CatDescription=db.StringField()
	Archived=db.BooleanField(default=False)
	UserCreated=db.StringField()
	DateCreated=db.StringField(default=str(datetime.datetime.now()))
	DateLastmodified=db.StringField()
	