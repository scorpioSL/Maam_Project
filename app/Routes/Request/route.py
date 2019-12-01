from flask import *
from flask_login import current_user,login_required
import json

RequestForms = Blueprint('requestForms', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---View Distributor Details---*******************
@RequestForms.route('/View_Distributor')
def view_Distributor():
	return render_template('Admin/Request/Distributor.html')



# ****************---View Supplier Details---*******************
@RequestForms.route('/View_Supplier')
def view_Supplier():
	return render_template('Admin/Request/Supplier.html')



# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

# ****************--- Distributor Application---*******************
@RequestForms.route('/Distributor_Application')
def Distributor_Application():
	return render_template('website/Request/DistributorApplication.html')






# ****************---Supplier Application---*******************
@RequestForms.route('/Supplier_Application',methods = ['GET','POST'])
def Supplier_Application():
	if request.method == 'POST':
		Name = request.form['Name']
		Address = request.form['Address']
		ContactNumber = request.form['ContactNumber']
		Email = request.form['Email']
		ProductList = json.loads(request.form['ProductList'])
		for Product in ProductList:
			print(Product["ProductName"])
		return jsonify(ProductList)
	return render_template('website/Request/SupplierApplication.html')