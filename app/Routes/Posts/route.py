from flask import *
from app import app
from werkzeug.utils import secure_filename
from flask_login import current_user,login_required

# Python Imports
import datetime
import os
import uuid

from app.database.models import Post,PostType

posts = Blueprint('Posts', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ********************---Add New Awards---*********************
@posts.route('/Add_Awards',methods = ['GET','POST'])
@login_required
def add_Awards():
	if request.method == 'POST':
		try:
			Title = request.form['TextBoxTitle']
			SubTitle = request.form['TextBoxSubTitle']
			Content = request.form['TextAreaContent']

			if Title == "" or SubTitle == "" or Content == "":
				Message = "Title or Subtitle or Content cannot be empty!"
				JsonResponse = {"Type":"Error","Message":Message}
				return jsonify(JsonResponse)
			PostImage = request.files['InputFieldImage']
			path = None
			# Uploading The Image
			if PostImage.filename != '' and PostImage:
				if PostImage.filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']:
					if not os.path.exists(current_app.root_path + app.config['IMAGES_FOLDER']):
						os.mkdir(current_app.root_path + app.config['IMAGES_FOLDER'])
					# Generating Unique ID For Image
					ImageID = uuid.uuid4()
					ImageID = str(ImageID)
					ImageID = ImageID.rsplit('-',1)
					ImageExt = PostImage.filename.rsplit('.',1)[1]
					NewImageName = "Awards_" + ImageID[1] + '.' + ImageExt
					PostImage.filename = NewImageName
					filename = secure_filename(PostImage.filename)
					PostImage.save(current_app.root_path + os.path.join(app.config['IMAGES_FOLDER'],filename))
					path = app.config['IMAGES_PATH'] + filename
			PostTypeObject = PostType.objects(PostTypeDescription = "Awards",Archived = False).first()
			if not PostTypeObject:
				Message = "Post type not found!"
				JsonResponse = {"Type" : "Error","Message" : Message}
				return jsonify(JsonResponse)
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject,UserCreated = current_user.UserName).save()
			Message = "Successfully Posted!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Posts/Awards.html')


# *******************---Add New Csr Events---******************
@posts.route('/Add_Csr', methods=['GET', 'POST'])
@login_required
def add_Csr():
	TitleOfPage = 'Post CSR'
	if request.method == 'POST':
		try:
			Title = request.form['TextBoxTitle']
			SubTitle = request.form['TextBoxSubTitle']
			Content = request.form['TextAreaContent']

			if Title == "" or SubTitle == "" or Content == "":
				Message = "Title or Subtitle or Content cannot be empty!"
				JsonResponse = {"Type":"Error","Message":Message}
				return jsonify(JsonResponse)
			PostImage = request.files['InputFieldImage']
			path = None
			# Uploading The Image
			if PostImage.filename != '' and PostImage:
				if PostImage.filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']:
					if not os.path.exists(current_app.root_path + app.config['IMAGES_FOLDER']):
						os.mkdir(current_app.root_path + app.config['IMAGES_FOLDER'])
					# Generating Unique ID For Image
					ImageID = uuid.uuid4()
					ImageID = str(ImageID)
					ImageID = ImageID.rsplit('-',1)
					ImageExt = PostImage.filename.rsplit('.',1)[1]
					NewImageName = "CSR_" + ImageID[1] + '.' + ImageExt
					PostImage.filename = NewImageName
					filename = secure_filename(PostImage.filename)
					PostImage.save(current_app.root_path + os.path.join(app.config['IMAGES_FOLDER'],filename))
					path =  app.config['IMAGES_PATH'] + filename
			PostTypeObject = PostType.objects(PostTypeDescription = "CSR",Archived = False).first()
			if not PostTypeObject:
				Message = "Post type not found!"
				JsonResponse = {"Type" : "Error","Message" : Message}
				return jsonify(JsonResponse)
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject,UserCreated = current_user.UserName).save()
			Message = "Successfully Posted!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Posts/CSR.html',TitleOfPage = TitleOfPage)

# Editing All The Posts(Types) In One Route
@posts.route('/Edit_POST/<PostID>/<currentURL>',methods = ['GET','POST'])
def edit_Post(PostID,currentURL):
	# Form Displaying Title Name
	PostTypeCheck = Post.objects(id = PostID).first()
	if PostTypeCheck and PostTypeCheck.PostType.PostTypeDescription == 'CSR':
		TitleOfPage = 'Edit CSR'
	elif PostTypeCheck and PostTypeCheck.PostType.PostTypeDescription == 'News':
		TitleOfPage = 'Edit News'
	else:
		TitleOfPage = 'Edit Awards'
	# Submiting From The Form request method will be post
	if request.method == 'POST':
		try:
			Title = request.form['TextBoxTitle']
			SubTitle = request.form['TextBoxSubTitle']
			Content = request.form['TextAreaContent']
			PostImage = request.files['InputFieldImage']
			# A Checkbox which will show in editing Post only. If its checked the PostImage attribute in MongoDB document have to remove
			DeleteImage = request.form.get('CheckboxDeleteCurrentImage')

			# Validation of required fields
			if Title == "" or Content == "":
				Message = "Title or Subtitle or Content cannot be empty!"
				JsonResponse = {"Type":"Error","Message":Message}
				return jsonify(JsonResponse)
			
			# A varibale to detemine image path
			path = None
			# Uploading The Image
			if PostImage.filename != '' and PostImage:
				if PostImage.filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']:
					if not os.path.exists(current_app.root_path + app.config['IMAGES_FOLDER']):
						os.mkdir(current_app.root_path + app.config['IMAGES_FOLDER'])
					# Generating Unique ID For Image
					ImageID = uuid.uuid4()
					ImageID = str(ImageID)
					ImageID = ImageID.rsplit('-',1)
					ImageExt = PostImage.filename.rsplit('.',1)[1]
					NewImageName = "CSR_" + ImageID[1] + '.' + ImageExt
					PostImage.filename = NewImageName
					filename = secure_filename(PostImage.filename)
					# Saving the image
					PostImage.save(current_app.root_path + os.path.join(app.config['IMAGES_FOLDER'],filename))
					path =  app.config['IMAGES_PATH'] + filename
					# Updating the database
					Post(id = PostID).update(set__PostTittle = Title,set__PostSubTitle = SubTitle,set__PostContent = Content,set__PostImage = path,set__UserModified = current_user.UserName,set__DateLastmodified = str(datetime.datetime.now()))
					# Returning responose to ajax request
					Message = "Successfully Updated!"
					JsonResponse = {"Type" : "Success","Message" : Message}
					return jsonify(JsonResponse)
			# If delete image checkbox is checked then DeleteImage variable will have a value else it will be None
			if DeleteImage:
				# Removing the PostImage attribute from Document as well as updating other data fields
				Post(id = PostID).update(set__PostTittle = Title,set__PostSubTitle = SubTitle,set__PostContent = Content,set__UserModified = current_user.UserName,set__DateLastmodified = str(datetime.datetime.now()),unset__PostImage = True)
				# Returning responose to ajax request
				Message = "Successfully Updated!"
				JsonResponse = {"Type" : "Success","Message" : Message}
				return jsonify(JsonResponse)
			# If DeleteImage doesn't have a value and neither the user didn't choose a new image then PostImage attribute doesn't need to update
			Post(id = PostID).update(set__PostTittle = Title,set__PostSubTitle = SubTitle,set__PostContent = Content,set__UserModified = current_user.UserName,set__DateLastmodified = str(datetime.datetime.now()))
			# Returning responose to ajax request
			Message = "Successfully Updated!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			# Exception returning
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	# Returning the object to the html to edit(When page is loading to edit/GET request)
	PostObj = Post.objects(id = PostID).first()
	# Creating a json object to return data since MongoDB document cannot convert to JSON(id field*)
	Obj = {'Title' : PostObj.PostTittle,'SubTitle':PostObj.PostSubTitle,'Content':PostObj.PostContent,'id':PostID,'URL':currentURL}
	return render_template('Admin/Posts/CSR.html',TitleOfPage = TitleOfPage,PostObj = Obj)



# ******************---Add News---*******************************
@posts.route('/Add_News',methods = ['GET','POST'])
@login_required
def add_News():
	if request.method == 'POST':
		try:
			Title = request.form['TextBoxTitle']
			SubTitle = request.form['TextBoxSubTitle']
			Content = request.form['TextAreaContent']

			if Title == "" or SubTitle == "" or Content == "":
				Message = "Title or Subtitle or Content cannot be empty!"
				JsonResponse = {"Type":"Error","Message":Message}
				return jsonify(JsonResponse)
			PostImage = request.files['InputFieldImage']
			path = None
			# Uploading The Image
			if PostImage.filename != '' and PostImage:
				if PostImage.filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']:
					if not os.path.exists(current_app.root_path + app.config['IMAGES_FOLDER']):
						os.mkdir(current_app.root_path + app.config['IMAGES_FOLDER'])
					# Generating Unique ID For Image
					ImageID = uuid.uuid4()
					ImageID = str(ImageID)
					ImageID = ImageID.rsplit('-',1)
					ImageExt = PostImage.filename.rsplit('.',1)[1]
					NewImageName = "News_" + ImageID[1] + '.' + ImageExt
					PostImage.filename = NewImageName
					filename = secure_filename(PostImage.filename)
					PostImage.save(current_app.root_path + os.path.join(app.config['IMAGES_FOLDER'],filename))
					path = app.config['IMAGES_PATH'] + filename
			PostTypeObject = PostType.objects(PostTypeDescription = "News",Archived = False).first()
			if not PostTypeObject:
				Message = "Post type not found!"
				JsonResponse = {"Type" : "Error","Message" : Message}
				return jsonify(JsonResponse)
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject,UserCreated = current_user.UserName).save()
			Message = "Successfully Posted!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Posts/News.html')



# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

# *********************************************
@posts.route('/Awards',methods = ['GET','POST'])
def awards():
	AwardsType = PostType.objects(PostTypeDescription = "Awards",Archived = False).first()
	AllAwards = None
	if AwardsType:
		AllAwards = Post.objects(PostType = AwardsType,Archived = False).order_by('-_id')
	return render_template('website/AboutUs/Awards.html',AllAwards = AllAwards,alert = 'No')



# *********************************************
@posts.route('/CsrDisplay')
def csrDisplay():
	CSRType = PostType.objects(PostTypeDescription = "CSR",Archived = False).first()
	AllCSR = None
	if CSRType:
		AllCSR = Post.objects(PostType = CSRType,Archived = False).order_by('-_id')
	return render_template('website/AboutUs/CsrDisplay.html',AllCSR = AllCSR)


# *********************************************
@posts.route('/NewsDisplay')
def newsDisplay():
	NewsType = PostType.objects(PostTypeDescription = "News",Archived = False).first()
	AllNews = None
	if NewsType:
		AllNews = Post.objects(PostType = NewsType,Archived = False).order_by('-_id')
	return render_template('website/AboutUs/News.html',AllNews = AllNews)


@posts.route('/UniquePost/<PostID>',methods = ['GET','POST'])
def UniquePost(PostID):
	UniquePost = Post.objects(id = PostID,Archived = False).first()
	if not UniquePost:
		abort(404)
	CSR = PostType.objects(PostTypeDescription = "CSR").first()
	News = PostType.objects(PostTypeDescription = "News").first()
	Awards = PostType.objects(PostTypeDescription = "Awards").first()
	if not CSR or not News or not Awards:
		abort(404)
	if UniquePost.PostType == CSR:
		Allcsr = [UniquePost]
		return render_template('website/AboutUs/CsrDisplay.html',AllCSR = Allcsr)
	elif UniquePost.PostType == News:
		AllNews = [UniquePost]
		return render_template('website/AboutUs/News.html',AllNews = AllNews)
	else:
		AllAwards = [UniquePost]
		return render_template('website/AboutUs/Awards.html',AllAwards = AllAwards)

@posts.route('/delete_post/<PostID>/<currentURL>',methods = ['GET','POST'])
@login_required
def DeletePost(PostID,currentURL):
	Post.objects(id = PostID).first().update(set__Archived = True)
	return redirect(url_for(currentURL,alert = 'Yes'))
