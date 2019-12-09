from flask import *
from flask_login import current_user,login_required
import json
from app.database.models import Supplier,RowMaterials,SupplierHasRowMaterials,Distributor,DistributorHasProducts,FinishedGood
from validate_email import validate_email

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
@RequestForms.route('/Distributor_Application',methods = ['GET','POST'])
def Distributor_Application():
	if request.method == 'POST':
		Name = request.form['Name']
		Address = request.form['Address']
		ContactNumber = request.form['ContactNumber']
		Email = request.form['Email']
		InvestmentAmount = request.form['InvestmentAmount']
		ProductList = json.loads(request.form['ProductList'])

		is_valid = validate_email(Email,verify=True)
  
		if not is_valid:
			Message = "Invalid Email!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
  
		if Name == "" or Address == "" or ContactNumber == "" or Email =="" or InvestmentAmount == "" or len(ProductList) == 0:
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		CheckDistributor = Distributor.objects(DistributorEmail = Email.lower(),Archived = False).first()
		if not CheckDistributor:
			CheckDistributor = Distributor(DistributorName = Name,DistributorAddress = Address,DistributorContactNumber = ContactNumber,DistributorEmail = Email.lower(),InvestmentAmount = InvestmentAmount).save()
		else:
			CheckDistributor = Distributor(id = CheckDistributor.id).update(InvestmentAmount = InvestmentAmount)
		for ProductItem in ProductList:
			FinishedGoodObj = FinishedGood.objects(id=ProductItem['ProductID'],Archived = False).first()
			if FinishedGoodObj:
				CheckBeforeObj = DistributorHasProducts.objects(Distributor = CheckDistributor,FinishedGood = FinishedGoodObj,Archived = False).first()
				if CheckBeforeObj:
					DistributorHasProducts(id = CheckBeforeObj.id).update(set__Quantity = ProductItem['Quantity'])
				else:
					DistributorHasProducts(Distributor = CheckDistributor,FinishedGood = FinishedGoodObj,Quantity = ProductItem['Quantity']).save()
			else:
				Message = "An Error Occured!, Please Contact Admin!"
				JsonResponse = {"Type": "Error", "Message": Message}
				return jsonify(JsonResponse)
		Message = "We recieved your request, We will get in touch with you soon via Email! Thank you!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
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
  
		is_valid = validate_email(Email,verify=True)
  
		if not is_valid:
			Message = "Invalid Email!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
  
		if Name == "" or Address == "" or ContactNumber == "" or Email =="" or len(RowMaterialList) == 0:
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		CheckSupplier = Supplier.objects(SupplierEmail = Email.lower(),Archived = False).first()
		if not CheckSupplier:
			CheckSupplier = Supplier(SupplierName = Name,SupplierAddress = Address,SupplierEmail = Email.lower(),SupplierContactNumber = ContactNumber).save()
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