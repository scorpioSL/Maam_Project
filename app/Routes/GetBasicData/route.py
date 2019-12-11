from flask import *
from app.database.models import *
from flask_login import current_user, login_required
import re

GetBasicData = Blueprint('GetBasicData', __name__)

@GetBasicData.route('/GetFinishedGoods',methods = ['GET'])
def GetFinishedGoodCategories():
    Categories = FinishedGoodCategory.objects(Archived = False)
    Data = []
    for Category in Categories:
        obj = {"id":str(Category.id),"CatDescription":Category.CatDescription}
        Data.append(obj)
    return(jsonify(Data))

@GetBasicData.route('/GetProductsDropDown',methods = ['GET'])
def GetProductsDropdown():
    Products = FinishedGood.objects(Archived = False)
    Data = []
    for Product in Products:
        obj = {"id":str(Product.id),"ItemName":Product.ItemName}
        Data.append(obj)
    return(jsonify(Data))

@GetBasicData.route('/GetRowMaterialsDropDown',methods = ['GET'])
def GetRowMaterialsDropdown():
    RowMaterialList = RowMaterials.objects(Archived = False)
    Data = []
    for RowMaterial in RowMaterialList:
        obj = {"id":str(RowMaterial.id),"ItemName":RowMaterial.RowMaterialDescription}
        Data.append(obj)
    return(jsonify(Data))



@GetBasicData.route('/GetProducts/<Search>',methods = ['GET','POST'])
@GetBasicData.route('/GetProducts',methods = ['GET'])
@GetBasicData.route('/GetProducts/ByCategory/<Category>',methods = ['GET','POST'])
def GetProducts(Search = None,Category = None):
    if not Search and not Category:
        Products = FinishedGood.objects(Archived = False)
    elif Category and not Search:
        ItemCategory = FinishedGoodCategory.objects(id = Category).first()
        Products = FinishedGood.objects(Archived = False,ItemCategory = ItemCategory)
    elif Search and not Category:
        Param = str.format('.*{}.*',Search)
        Regex = re.compile(Param,re.IGNORECASE)
        Products = FinishedGood.objects(Archived = False,ItemName = Regex)
    Data = []
    for Product in Products:
        obj = {'ItemCode':Product.ItemCode,'ItemName':Product.ItemName,'ItemUnit':Product.ItemUnit,'ItemPrice':Product.ItemPrice,'ItemCategory':Product.ItemCategory.CatDescription,'ItemImagePath':Product.ItemImagePath}
        Data.append(obj)
    return(jsonify(Data))

@GetBasicData.route('/GetProducts/AutoComplete/<SearchingText>',methods = ['GET','POST'])
def GetProductAutoComplete(SearchingText = None):
    Data = []
    if SearchingText:
        Param = str.format('.*{}.*',SearchingText)
        Regex = re.compile(Param,re.IGNORECASE)
        Products = FinishedGood.objects(Archived = False,ItemName = Regex)
        for Product in Products:
            obj = {'ItemCode':Product.ItemCode,'ItemName':Product.ItemName,'ItemUnit':Product.ItemUnit,'ItemPrice':Product.ItemPrice,'ItemCategory':Product.ItemCategory.CatDescription,'ItemImagePath':Product.ItemImagePath}
            Data.append(obj)
        return jsonify(Data)


@GetBasicData.route('/GetNewReleases',methods = ['GET'])
def GetNewReleases():
    Data = []
    Products = FinishedGood.objects(Archived = False).order_by('-_id')
    count = 0
    if Products.count() >= 3:
        for Product in Products:
            count = count + 1
            obj = {'ItemCode':Product.ItemCode,'ItemName':Product.ItemName,'ItemUnit':Product.ItemUnit,'ItemPrice':Product.ItemPrice,'ItemCategory':Product.ItemCategory.CatDescription,'ItemImagePath':Product.ItemImagePath}
            Data.append(obj)
            if count == 3:
                break
    return(jsonify(Data))


@GetBasicData.route('/SetProductAutocompleteSelected/<ProductName>',methods = ['POST','GET'])
@login_required
def SetProductAutoCompleteSelected(ProductName):
    Product = FinishedGood.objects(Archived = False,ItemName = ProductName).first()
    if not Product:
        obj = {"Message":"Error"}
        return jsonify(obj)
    FinishedGoodsCategories = FinishedGoodCategory.objects(Archived = False)
    index = 0
    for FinishedGoodCategoryObj in FinishedGoodsCategories:
        if FinishedGoodCategoryObj.CatDescription == Product.ItemCategory.CatDescription:
            break
        index = index + 1
    obj = {"Message":"Success","ItemID":str(Product.id),"ItemCode":Product.ItemCode,"ItemName":Product.ItemName,"Unit":Product.ItemUnit,"Price":Product.ItemPrice,"ItemCategoryIndex":index,"ImagePath":Product.ItemImagePath}
    return jsonify(obj)