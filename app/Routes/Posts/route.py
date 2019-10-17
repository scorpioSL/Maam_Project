from flask import *
from app import app
from werkzeug.utils import secure_filename

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
@posts.route('/Add_Awards')
def add_Awards():
	return render_template('Admin/Posts/Awards.html')


# *******************---Add New Csr Events---******************
@posts.route('/Add_Csr', methods=['GET', 'POST'])
def add_Csr():
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
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject).save()
			Message = "Successfully Posted!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Posts/CSR.html')



# ******************---Add News---*******************************
@posts.route('/Add_News',methods = ['GET','POST'])
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
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject).save()
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
			Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject).save()
			Message = "Successfully Posted!"
			JsonResponse = {"Type" : "Success","Message" : Message}
			return jsonify(JsonResponse)
		except:
			Message = "An error occured!"
			JsonResponse = {"Type" : "Error","Message" : Message}
			return jsonify(JsonResponse)
	return render_template('website/AboutUs/Awards.html')



# *********************************************
@posts.route('/CsrDisplay')
def csrDisplay():
	CSRType = PostType.objects(PostTypeDescription = "CSR").first()
	AllCSR = Post.objects(PostType = CSRType,Archived = False).order_by('-_id')
	return render_template('website/AboutUs/CsrDisplay.html',AllCSR = AllCSR)


# *********************************************
@posts.route('/NewsDisplay')
def newsDisplay():
	return render_template('website/AboutUs/News.html')
