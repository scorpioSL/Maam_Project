from flask import *
from app.database.models import User,UserType,PostType,FinishedGoodCategory
from app import bcrypt
from app import LoginManager
from flask_login import login_user, current_user, logout_user, login_required

admin = Blueprint('Authentication', __name__)


# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# **********************---Login---***************************
@admin.route('/login',methods = ['GET','POST'])
def login():
	if current_user.is_authenticated:
		# If User Is ALready Logged In Redirect The user
		return redirect(url_for('dashboard'))
	ShowAlert = False
	if request.method == 'POST':
		Username = request.form['Username']
		Password = request.form['Password']
		remember = True
		CheckUser = User.objects(UserName = Username).first()
		if CheckUser:
			if bcrypt.check_password_hash(CheckUser.UserPassword,Password):
				login_user(CheckUser, remember = remember)
				Message = 'Success'
				JsonResponse = {'Type':'Success','Message':Message}
				return jsonify(JsonResponse)
		Message = 'Invalid Username or password!'
		JsonResponse = {'Type':'Warning','Message':Message}
		return jsonify(JsonResponse)

	if 'ShowAlert' in request.args:
		ShowAlert = request.args['ShowAlert']
	return render_template('Admin/Authentication/authentication-login.html',ShowAlert = ShowAlert)


# *********************---User Register---********************
@admin.route('/register',methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		# If User Is ALready Logged In Redirect The user
		return redirect(url_for('dashboard'))
	if request.method == 'POST':
		# Checking wether UserTypes exhist or not, If not add to db
		CheckUserTypes = UserType.objects().count()
		if CheckUserTypes < 1:
			UserType(TypeDescription = "Admin",UserCreated = "Auto Generated!").save()
			UserType(TypeDescription = "User",UserCreated = "Auto Generated!").save()
			PostType(PostTypeDescription = "CSR",UserCreated = "Auto Generated!").save()
			PostType(PostTypeDescription = "News",UserCreated = "Auto Generated!").save()
			PostType(PostTypeDescription = "Awards",UserCreated = "Auto Generated!").save()
			print("UserTypes Created!")
		Username = request.form['Username']
		Password = request.form['Password']
		# # Bcrypt password
		HashedPassword = bcrypt.generate_password_hash(Password)
		# #Check Db Records
		CheckUsername= User.objects(UserName=Username).first()
		if CheckUsername:
			Message = "Username already taken!"
			JsonResponse = {'Type':'Warning','Message':Message}
			return jsonify(JsonResponse)
		CountUsers = User.objects().count()
		if CountUsers > 0:
			UserTypeObj = UserType.objects(TypeDescription = "User").first()
			User(UserName = Username,UserPassword = HashedPassword,UserType = UserTypeObj,UserCreated = str(User.objects().first().UserName)).save()
			Message = "Successfully registered!"
			JsonResponse = {'Type':"Success",'Message':Message}
			return jsonify(JsonResponse)
		else:
			UserTypeObj = UserType.objects(TypeDescription = "Admin").first()
			User(UserName = Username,UserPassword = HashedPassword,UserType = UserTypeObj ,UserAccess = True,UserCreated = None).save()
			Message = "Successfully registered! (Admin)"
			JsonResponse = {'Type':"Success",'Message':Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Authentication/authentication-register.html')


# <!-- ============================================================== -->#
@admin.route('/forgot')
def forgot():
	return render_template('Admin/Authentication/forgotPassword.html')

@admin.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('Authentication.login'))


# *****************---Dashboard---****************************
@admin.route('/dashboard')
@login_required
def dashboard():
	return render_template('Admin/Dashboard/index.html')


@admin.route('/AddCategories')
def AddCategory():
	FinishedGoodCategory(CatDescription="Chocolate").save()
	FinishedGoodCategory(CatDescription="Vanilla").save()
	FinishedGoodCategory(CatDescription="Strawberry").save()
	return 'Success'