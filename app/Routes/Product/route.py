from flask import *
from app.database.models import FinishedGoodCategory, FinishedGood
from flask_login import current_user, login_required
from app import app
from app.MyFunctions import SaveImage
import datetime

product = Blueprint('Product', __name__)


# ------------------------------------------------------------------
# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---Add New Product---*************************
@product.route('/Add_Product', methods=['GET', 'POST'])
@login_required
def add_Product():
	if request.method == 'POST':
		ItemCode = request.form['TextBoxItemCode']
		ProductName = request.form['TextBoxProductName']
		Unit = request.form['TextBoxUnit']
		Price = request.form['TextBoxPrice']
		ProductImage = request.files['InputFieldImage']
		ItemCategoryId = request.form['DropDownListItemCategory']
		Category = FinishedGoodCategory.objects(id=ItemCategoryId).first()
		if not Category:
			Message = "Product Category not found!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		# Required Fields Validation
		if ItemCode == "" or ProductName == "" or Unit == "" or Price == "" or ProductImage.filename == "":
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		DuplicateCheck = FinishedGood.objects(ItemCode=ItemCode).first()
		if DuplicateCheck:
			Message = "A product with same ItemCode already added!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		ImageFolderPath = '/static/Images/ProductImages/'
		Path = SaveImage(app, current_app, ProductImage,
						 ImageFolderPath, 'PR_')
		FinishedGood(ItemCode=ItemCode, ItemName=ProductName, ItemUnit=Unit, ItemPrice=Price,
					 ItemCategory=Category, ItemImagePath=Path, UserCreated=current_user.UserName).save()
		Message = "Successfully added!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
	return render_template('Admin/Product/productForm.html')


# ****************---Edit Product Details---************************
@product.route('/Edit_Product', methods=['GET', 'POST'])
@login_required
def edit_Product():
	if request.method == 'POST':
		ItemCode = request.form['TextBoxItemCode']
		ProductName = request.form['TextBoxProductName']
		Unit = request.form['TextBoxUnit']
		Price = request.form['TextBoxPrice']
		ProductImage = request.files['ImageFieldImage']
		ItemCategoryId = request.form['DropDownListItemCategory']
		Category = FinishedGoodCategory.objects(id=ItemCategoryId).first()
		if not Category:
			Message = "Product Category not found!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		# Required Fields Validation
		if ItemCode == "" or ProductName == "" or Unit == "" or Price == "":
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		
		UpdateObj = FinishedGood.objects(ItemCode = ItemCode,Archived = False).first()
		DuplicateCheck = FinishedGood.objects(ItemCode=ItemCode,Archived = False).first()
		if DuplicateCheck != UpdateObj:
			Message = "A product with same ItemCode already added!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		
		if ProductImage.filename:
			ImageFolderPath = '/static/Images/ProductImages/'
			Path = SaveImage(app, current_app, ProductImage,ImageFolderPath, 'PR_')
			FinishedGood(id=UpdateObj.id).update(set__ItemCode=ItemCode, set__ItemName=ProductName, set__ItemUnit=Unit, set__ItemPrice=Price,set__ItemCategory=Category, set__ItemImagePath=Path,set__UserModified=current_user.UserName, set__DateLastmodified=str(datetime.datetime.now()))
			Message = "Successfully added!"
			JsonResponse = {"Type": "Success", "Message": Message}
			return jsonify(JsonResponse)
		else:
			FinishedGood(id=UpdateObj.id).update(set__ItemCode=ItemCode, set__ItemName=ProductName, set__ItemUnit=Unit, set__ItemPrice=Price,set__ItemCategory=Category, set__UserModified=current_user.UserName, set__DateLastmodified=str(datetime.datetime.now()))
			Message = "Successfully added!"
			JsonResponse = {"Type": "Success", "Message": Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Product/EditProduct.html')


<<<<<<< HEAD
<<<<<<< HEAD
# ****************---Add new Category---************************
@product.route('/Add_category')
def add_category():
	return render_template('Admin/Product/AddCategory.html')


=======
=======
>>>>>>> 60be91f805dcc9754fa07fdb02b83e916805303c
@product.route('/DeleteProduct/<ItemCode>',methods = ['GET','POST'])
@login_required
def DeleteProduct(ItemCode):
    DeleteProduct = FinishedGood.objects(ItemCode = ItemCode,Archived = False).first()
    if not DeleteProduct:
        Message = "Product not found!"
        JsonResponse = {"Type":"Error","Message":Message}
        return jsonify(JsonResponse)
    FinishedGood(id = DeleteProduct.id).update(set__Archived = True)
    Message = "Success"
    JsonResponse = {"Type":"Success","Message":Message}
    return jsonify(JsonResponse)


# ------------------------------------------------------------------
	# WEBSITE FUNCTIONS
<<<<<<< HEAD
>>>>>>> 60be91f805dcc9754fa07fdb02b83e916805303c
=======
>>>>>>> 60be91f805dcc9754fa07fdb02b83e916805303c
# ------------------------------------------------------------------
