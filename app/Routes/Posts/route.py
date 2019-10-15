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
@posts.route('/Add_Csr')
def add_Csr():
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