from flask import *
from app import app
from app.MyFunctions import SaveImage
from app.database.models import Department, Vacancy, Applicant
from flask_login import current_user, login_required
import datetime
import os
import uuid

vacancy = Blueprint('Vacancy', __name__)

# ------------------------------------------------------------------
# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# ******************---Add Vacancy---*****************************
@vacancy.route('/Vacancy', methods=['GET', 'POST'])
@login_required
def add_Vacancy():
	if request.method == 'POST':
		JobTitle = request.form['JobTitle']
		DepartmentInput = request.form['DropDownListDepartment']
		FileFieldJobAdvertistment = request.files['FileFieldJobAdvertistment']
		DepartmentObj = Department.objects(
			id=DepartmentInput, Archived=False).first()
		if JobTitle == "" or DepartmentInput == "" or not FileFieldJobAdvertistment or FileFieldJobAdvertistment.filename == "":
			Message = "All data must be filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		if not DepartmentObj:
			Message = "Error, Please contact the developers.(Department 404)"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		ImageFolderPath = '/static/Images/Vacancy/'
		Path = SaveImage(app, current_app,
						 FileFieldJobAdvertistment, ImageFolderPath, 'VC_')
		Vacancy(Tittle=JobTitle, Department=DepartmentObj, Poster=Path).save()
		Message = "Successfully Saved!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
	return render_template('Admin/Vacancy/vacancy.html')


# ****************---Edit Vacancy Details---************************
@vacancy.route('/Edit_Vacancy', methods=['GET', 'POST'])
@login_required
def edit_Vacancy():
	if request.method == 'POST':
		objId = request.form['TextBoxItemId']
		JobTitle = request.form['JobTitle']
		DepartmentInput = request.form['DropDownListDepartment']
		FileFieldJobAdvertistment = request.files['FileFieldJobAdvertistment']

		UpdateObj = Vacancy.objects(id=objId, Archived=False).first()
		if not UpdateObj:
			Message = "Error. Please Contact Developers(404 UpdateObj)"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		if JobTitle == "" or DepartmentInput == "":
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		DepartmentObj = Department.objects(
			id=DepartmentInput, Archived=False).first()
		if not DepartmentObj:
			Message = "Error, Please contact the developers.(Department 404)"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		if FileFieldJobAdvertistment.filename:
			ImageFolderPath = '/static/Images/Vacancy/'
			Path = SaveImage(app, current_app,
							 FileFieldJobAdvertistment, ImageFolderPath, 'VC_')
			Vacancy(id=UpdateObj.id).update(set__Tittle=JobTitle, set__Department=DepartmentObj, set__Poster=Path,
											set__UserModified=current_user.UserName, set__DateLastmodified=str(datetime.datetime.now()))
			Message = "Successfully added!"
			JsonResponse = {"Type": "Success", "Message": Message}
			return jsonify(JsonResponse)
		else:
			Vacancy(id=UpdateObj.id).update(set__Tittle=JobTitle, set__Department=DepartmentObj,
											set__UserModified=current_user.UserName, set__DateLastmodified=str(datetime.datetime.now()))
			Message = "Successfully added!"
			JsonResponse = {"Type": "Success", "Message": Message}
			return jsonify(JsonResponse)
	return render_template('Admin/Vacancy/EditVacancy.html')


@vacancy.route('/DeleteVacancy/<VacancyId>', methods=['GET', 'POST'])
@login_required
def delete_Vacancy(VacancyId):
	VacancyObj = Vacancy.objects(id=VacancyId, Archived=False).first()
	if not VacancyObj:
		Message = "Vacancy not found!"
		JsonResponse = {"Type": "Error", "Message": Message}
		return jsonify(JsonResponse)
	Vacancy(id=VacancyObj.id).update(set__Archived=True)
	Message = "Success!"
	JsonResponse = {"Type": "Success", "Message": Message}
	return jsonify(JsonResponse)


@vacancy.route('/GetAllVacancies', methods=['GET'])
def getallVacancies():
	Vacancies = Vacancy.objects(Archived=False).order_by('-_id')
	Data = []
	for vacancy in Vacancies:
		obj = {"Id": str(vacancy.id), "Title": vacancy.Tittle, "Department": vacancy.Department.DepDescription,
			   "Poster": vacancy.Poster, "Date": vacancy.DateCreated[0:11]}
		Data.append(obj)
	return jsonify(Data)

# *****************---View Applicant Details---*******************
@vacancy.route('/View_Applicant')
@login_required
def view_Applicant():
	return render_template('Admin/Vacancy/Applicant.html')

# *****************---Add Department Details---*******************
@vacancy.route('/Add_Department')
@login_required
def add_Department():
	return render_template('Admin/Vacancy/AddDepartment.html')


# ------------------------------------------------------------------
	# WEBSITE FUNCTIONS
# ------------------------------------------------------------------

@vacancy.route('/View_Career')
def view_Career():
	return render_template('website/Career/Career.html')


@vacancy.route('/Job_Application', methods=['GET', 'POST'])
def job_Application():
	if request.method == 'POST':
		Name = request.form['Name']
		Address = request.form['Address']
		Contact = request.form['Contact']
		Email = request.form['Email']
		AcademicQuali = request.form['AcademicQuali']
		OtherQuali = request.form['OtherQuali']
		Experience = request.form['Experience']
		UploadCV = request.files['CV']

		if not os.path.exists(current_app.root_path + current_app.config['CV_PATH']):
			os.mkdir(current_app.root_path + current_app.config['CV_PATH'])

		Extention = UploadCV.filename.rsplit('.', 1)[1]
		FileName = Email + str(uuid.uuid4()) + '.' + Extention
		UploadCV.filename = FileName
		UploadCV.save(current_app.root_path +
					  os.path.join(current_app.config['CV_PATH'], UploadCV.filename))

		Path = os.path.join(current_app.config['CV_PATH'], UploadCV.filename)
		Applicant(ApplicantName=Name, ApplicantAddress=Address, ApplicantEmail=Email, ApplicantNumber=Contact,
				  ApplicantAcadamicQuali=AcademicQuali, ApplicantOtherQuali=OtherQuali, ApplicantExperience=Experience, ApplicantCV=Path).save()
		Message = "We recieved your application!, We'll contact you soon!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
	return render_template('website/Career/ApplicationForm.html')


@vacancy.route('/View_Vacancy')
def view_Vacancy():
	return render_template('website/Career/Vacancy.html')
