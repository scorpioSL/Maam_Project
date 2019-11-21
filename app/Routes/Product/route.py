from flask import *
from flask_login import current_user,login_required

product = Blueprint('Product', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---Add New Product---*************************
@product.route('/Add_Product',methods = ['GET','POST'])
@login_required
def add_Product():
	if request.method == 'POST':
		ItemCode = request.form['SelectedFieldValue']
		return ItemCode
	return render_template('Admin/Product/productForm.html')


# ****************---Edit Product Details---************************
@product.route('/Edit_Product')
@login_required
def edit_Product():
	return render_template('Admin/Product/EditProduct.html')


# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------