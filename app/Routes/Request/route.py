from flask import *

request = Blueprint('Request', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---View Distributor Details---*******************
@request.route('/View_Distributor')
def view_Distributor():
	return render_template('Admin/Request/Distributor.html')



# ****************---View Supplier Details---*******************
@request.route('/View_Supplier')
def view_Supplier():
	return render_template('Admin/Request/Supplier.html')



# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

# ****************--- Distributor Application---*******************
@request.route('/Distributor_Application')
def Distributor_Application():
	return render_template('website/Request/DistributorApplication.html')






# ****************---Supplier Application---*******************
@request.route('/Supplier_Application')
def Supplier_Application():
	return render_template('website/Request/SupplierApplication.html')