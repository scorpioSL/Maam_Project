from flask import *

product = Blueprint('Product', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ****************---Add New Product---*************************
@product.route('/Add_Product')
def add_Product():
	return render_template('Admin/Product/ProductForm.html')


# ****************---Edit Product Details---************************
@product.route('/Edit_Product')
def edit_Product():
	return render_template('Admin/Product/EditProduct.html')


# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------