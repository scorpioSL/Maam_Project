from flask import *
from app.database.models import FinishedGoodCategory,FinishedGood
from flask_login import current_user,login_required
from app import app
from app.MyFunctions import SaveImage

product = Blueprint('Product', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---Add New Product---*************************
@product.route('/Add_Product',methods = ['GET','POST'])
@login_required
def add_Product():
	if request.method == 'POST':
		ItemCode = request.form['TextBoxItemCode']
		ProductName = request.form['TextBoxProductName']
		Unit = request.form['TextBoxUnit']
		Price = request.form['TextBoxPrice']
		ProductImage = request.files['InputFieldImage']
		ItemCategoryId = request.form['DropDownListItemCategory']
		Category = FinishedGoodCategory.objects(id = ItemCategoryId).first()
		if not Category:
			Message = "Product Category not found!"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)

		# Required Fields Validation
		if ItemCode == "" or ProductName == "" or Unit == "" or Price == "" or ProductImage.filename == "":
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)

		DuplicateCheck = FinishedGood.objects(ItemCode = ItemCode).first()
		if DuplicateCheck:
			Message = "A product with same ItemCode already added!"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)

		ImageFolderPath = '/static/Images/ProductImages/'
		Path = SaveImage(app,current_app,ProductImage,ImageFolderPath,'PR_')
		FinishedGood(ItemCode = ItemCode,ItemName = ProductName,ItemUnit = Unit,ItemPrice = Price,ItemCategory = Category,ItemImagePath = Path,UserCreated = current_user.UserName).save()
		Message = "Successfully added!"
		JsonResponse = {"Type" : "Success","Message" : Message}
		return jsonify(JsonResponse)
	return render_template('Admin/Product/productForm.html')


# ****************---Edit Product Details---************************
@product.route('/Edit_Product')
@login_required
def edit_Product():
	return render_template('Admin/Product/EditProduct.html')


# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------