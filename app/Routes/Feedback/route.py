from flask import*

feedback = Blueprint('Feedback', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# *****************---View Inquries---****************************
@feedback.route('/View_Inquries')
def view_Inquries():
	return render_template('Admin/Feedback/Inquries.html')








# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------