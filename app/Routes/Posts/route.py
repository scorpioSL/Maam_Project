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
		Title = request.form['TextBoxTitle']
		SubTitle = request.form['TextBoxSubTitle']
		Content = request.form['TextAreaContent']

		if Title == "" or SubTitle == "" or Content == "":
			Message = "Title or Subtitle or Content cannot be empty!"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)
		PostImage = request.files['InputFieldImage']
		path = current_app.root_path + app.config['IMAGES_FOLDER'] + "default.jpg"
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
				NewImageName = ImageID[1] + '.' + ImageExt
				PostImage.filename = NewImageName
				filename = secure_filename(PostImage.filename)
				PostImage.save(current_app.root_path + os.path.join(app.config['IMAGES_FOLDER'],filename))
				path = current_app.root_path + app.config['IMAGES_FOLDER'] + filename
		PostTypeObject = PostType.objects(PostTypeDescription = "CSR").first()
		Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage = path,PostType = PostTypeObject).save()
		Message = "Successfully Posted!"
		JsonResponse = {"Type" : "Success","Message" : Message}
		return jsonify(JsonResponse)
	return render_template('Admin/Posts/CSR.html')



# ******************---Add News---*******************************
@posts.route('/Add_News')
def add_News():
	return render_template('Admin/Posts/News.html')



# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

# *********************************************
@posts.route('/Awards')
def awards():
	return render_template('website/AboutUs/Awards.html')



# *********************************************
@posts.route('/CsrDisplay')
def csrDisplay():
	return render_template('website/AboutUs/CsrDisplay.html')


# *********************************************
@posts.route('/NewsDisplay')
def newsDisplay():
	return render_template('website/AboutUs/News.html')
