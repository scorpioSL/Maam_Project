from flask import *
from app.database.models import *
from flask_login import current_user, login_required

GetBasicData = Blueprint('GetBasicData', __name__)

@GetBasicData.route('/GetFinishedGoods',methods = ['GET'])
@login_required
def GetFinishedGoodCategories():
    Categories = FinishedGoodCategory.objects(Archived = False)
    Data = []
    for Category in Categories:
        obj = {"id":str(Category.id),"CatDescription":Category.CatDescription}
        Data.append(obj)
    return(jsonify(Data))