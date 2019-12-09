from flask import *
from app.database.models import *
from flask_login import current_user, login_required
import re


# This File Is Only For Testing Purpose. Do Not Use On Production Server

TestData = Blueprint('TestData', __name__)

@TestData.route('/AddRowMaterials',methods = ['GET'])
def AddRowMaterials():
    RowMaterials(RowMaterialDescription = "Sugar").save()
    RowMaterials(RowMaterialDescription = "Flour").save()
    RowMaterials(RowMaterialDescription = "Vanilla").save()
    RowMaterials(RowMaterialDescription = "Chocolate").save()
    return "Done"

@TestData.route('/AddFeedBackTypes',methods = ['GET'])
def AddFeedBackTypes():
    FeedbackType(Description = "Feedback").save()
    FeedbackType(Description = "Inquiry").save()
    FeedbackType(Description = "Other").save()
    return "Done"