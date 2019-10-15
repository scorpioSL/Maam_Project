from flask import*

website = Blueprint('Website', __name__)


##############################________Website Routes________###################################





# *********************************************
@website.route('/CompanyOverview')
def companyOverview():
	return render_template('website/AboutUs/CompanyOverview.html')


# *********************************************
@website.route('/ContactUs')
def contactUs():
	return render_template('website/ContactUs.html')


# *********************************************
@website.route('/Heritage')
def heritage():
	return render_template('website/AboutUs/Heritage.html')


# *********************************************
@website.route('/Home')
def home():
	return render_template('website/AboutUs/Home.html')





# *********************************************
@website.route('/ProductDisplay')
def productDisplay():
	return render_template('website/ProductDisplay.html')


# *********************************************
@website.route('/Vision')
def vision():
	return render_template('website/Vision.html')



