from flask import *
from flask_login import current_user,login_required
import json
from app.database.models import Supplier,RowMaterials,SupplierHasRowMaterials

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
		RowMaterialList = json.loads(request.form['RowMaterialList'])
		if Name == "" or Address == "" or ContactNumber == "" or Email =="" or len(RowMaterialList) == 0:
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		CheckSupplier = Supplier.objects(SupplierEmail = Email,Archived = False).first()
		if not CheckSupplier:
			CheckSupplier = Supplier(SupplierName = Name,SupplierAddress = Address,SupplierEmail = Email,SupplierContactNumber = ContactNumber).save()
		for RowMaterial in RowMaterialList:
			RowMaterialObj = RowMaterials.objects(id=RowMaterial['RowMaterialID'],Archived = False).first()
			if RowMaterialObj:
				CheckBeforeObj = SupplierHasRowMaterials.objects(Supplier = CheckSupplier,RowMaterial = RowMaterialObj,Archived = False).first()
				if CheckBeforeObj:
					SupplierHasRowMaterials(id = CheckBeforeObj.id).update(set__Price = RowMaterial['Price'])
				else:
					SupplierHasRowMaterials(Supplier = CheckSupplier,RowMaterial = RowMaterialObj,Price = RowMaterial['Price']).save()
			else:
				Message = "An Error Occured!, Please Contact Admin!"
				JsonResponse = {"Type": "Error", "Message": Message}
				return jsonify(JsonResponse)
		Message = "We recieved your request, We will get in touch with you soon via Email! Thank you!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
	return render_template('website/Request/SupplierApplication.html')