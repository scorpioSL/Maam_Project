from flask import *
from app import app
from app.MyFunctions import SaveImage
from app.database.models import Department,Vacancy

vacancy = Blueprint('Vacancy', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ******************---Add Vacancy---*****************************
@vacancy.route('/Vacancy')
def add_Vacancy():
    if request.method == 'POST':
        JobTitle = request.form['JobTitle']
        DepartmentInput = request.form['DropDownListDepartment']
        FileFieldJobAdvertistment = request.form['FileFieldJobAdvertistment']
        return Department
	return render_template('Admin/Vacancy/vacancy.html')


# ****************---Edit Vacancy Details---************************
@vacancy.route('/Edit_Vacancy')
def edit_Vacancy():
	return render_template('Admin/Vacancy/EditVacancy.html')


# *****************---View Applicant Details---*******************
@vacancy.route('/View_Applicant')
def view_Applicant():
	return render_template('Admin/Vacancy/Applicant.html')


# ******************---Add Department---*****************************
@vacancy.route('/Add_Department')
def add_Department():
	return render_template('Admin/Vacancy/Department.html')

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

