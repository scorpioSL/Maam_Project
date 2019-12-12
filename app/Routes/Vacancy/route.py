from flask import *
from app import app
from app.MyFunctions import SaveImage
from app.database.models import Department,Vacancy

vacancy = Blueprint('Vacancy', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ******************---Add Vacancy---*****************************
@vacancy.route('/Vacancy',methods = ['GET','POST'])
def add_Vacancy():
	if request.method == 'POST':
		JobTitle = request.form['JobTitle']
		DepartmentInput = request.form['DropDownListDepartment']
		FileFieldJobAdvertistment = request.files['FileFieldJobAdvertistment']
		DepartmentObj = Department.objects(id = DepartmentInput).first()
		if JobTitle == "" or DepartmentInput == "" or not FileFieldJobAdvertistment or FileFieldJobAdvertistment.filename == "":
			Message = "All data must be filled!"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)

		if not DepartmentObj:
			Message = "Error, Please contact the developers.(Department 404)"
			JsonResponse = {"Type":"Error","Message":Message}
			return jsonify(JsonResponse)
		ImageFolderPath = '/static/Images/Vacancy/'
		Path = SaveImage(app, current_app, FileFieldJobAdvertistment,ImageFolderPath, 'VC_')
		Vacancy(Tittle = JobTitle,Department = DepartmentObj,Poster = Path).save()
		Message = "Successfully Saved!"
		JsonResponse = {"Type":"Success","Message":Message}
		return jsonify(JsonResponse)
	return render_template('Admin/Vacancy/vacancy.html')


# ****************---Edit Vacancy Details---************************
@vacancy.route('/Edit_Vacancy')
def edit_Vacancy():
	return render_template('Admin/Vacancy/EditVacancy.html')


# *****************---View Applicant Details---*******************
@vacancy.route('/View_Applicant')
def view_Applicant():
	return render_template('Admin/Vacancy/Applicant.html')

# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

@vacancy.route('/View_Career')
def view_Career():
	return render_template('website/Career/Career.html')

@vacancy.route('/Job_Application')
def job_Application():
	return render_template('website/Career/ApplicationForm.html')

@vacancy.route('/View_Vacancy')
def view_Vacancy():
	return render_template('website/Career/Vacancy.html')

