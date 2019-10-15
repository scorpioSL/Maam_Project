from flask import *

request = Blueprint('Request', __name__)


# ****************---View Distributor Details---*******************
@request.route('/View_Distributor')
def view_Distributor():
	return render_template('Admin/Request/Distributor.html')



# ****************---View Supplier Details---*******************
@request.route('/View_Supplier')
def view_Supplier():
	return render_template('Admin/Request/Supplier.html')
