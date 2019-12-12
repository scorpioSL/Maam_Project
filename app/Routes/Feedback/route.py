from flask import*
from validate_email import validate_email
from app.database.models import Feedback,FeedbackType
feedback = Blueprint('Feedback', __name__)

# ------------------------------------------------------------------
						# ADMIN FUNCTIONS
# ------------------------------------------------------------------

# *****************---View Inquries---****************************
@feedback.route('/View_Inquries')
def view_Inquries():
	return render_template('Admin/Feedback/Inquries.html')








# ------------------------------------------------------------------
						# WEBSITE FUNCTIONS
# ------------------------------------------------------------------
@feedback.route('/ContactUs',methods = ['GET','POST'])
def ContactUs():
	if request.method == 'POST':
		Name = request.form['Name']
		Email = request.form['Email']
		Country = request.form['Country']
		Subject = request.form['Subject']
		Message = request.form['Message']
		FeedBackType = request.form['FeedBackType']
		
		is_valid = validate_email(Email,verify=True)
  
		if not is_valid:
			Message = "Invalid Email!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)

		if Name == "" or Email == "" or Country == "" or Subject == "" or Message == "":
			Message = "All Fields Must Be Filled!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		FeedBackTypeObj = FeedbackType.objects(id = FeedBackType).first()
		if not FeedBackTypeObj:
			Message = "An Error Occured!, Please Contact The Devolopers!"
			JsonResponse = {"Type": "Error", "Message": Message}
			return jsonify(JsonResponse)
		Feedback(Name = Name,Country = Country,Email = Email.lower(),Message = Message,Subject = Subject,FeedbackType = FeedBackTypeObj).save()
		Message = "Your FeedBack Has Been Saved Successfully!, We Will Get In Touch With You Soon!, Thank You!"
		JsonResponse = {"Type": "Success", "Message": Message}
		return jsonify(JsonResponse)
	return render_template('website/ContactUs.html')