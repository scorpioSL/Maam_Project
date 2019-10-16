from flask import *

posts = Blueprint('Posts', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ********************---Add New Awards---*********************
@posts.route('/Add_Awards')
def add_Awards():
	return render_template('Admin/Posts/Awards.html')


# *******************---Add New Csr Events---******************
# Have To save image in server and send to the db
@posts.route('/Add_Csr',methods = ['GET','POST'])
def add_Csr():
	if request.method == 'POST':
		Title = request.form['TextBoxTitle']
		SubTitle = request.form['TextBoxSubTitle']
		Content = request.form['TextAreaContent']
		PostImage = request.files['InputFieldImage']
		PostTypeObject = PostType.objects(PostTypeDescription = "CSR").first()
		# Post(PostTittle = Title,PostSubTitle = SubTitle,PostContent = Content,PostImage,PostType = PostTypeObject).save()
	path = current_app.root_path
	return render_template('Admin/Posts/CSR.html',path = path)



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