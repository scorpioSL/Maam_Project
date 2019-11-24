from werkzeug.utils import secure_filename
import os
import uuid


def SaveImage(app,current_app,FileField,ImageFolderPath,ImageName):
    '''
        Takes app,current_app,FileField,ImageFolderPath,ImageName as Parameters
        ImageFolderPath = /static/Images -> Must have Static Part
        Returns the path of the saved file without static part
    '''
    if FileField.filename != '' and FileField:
        # Validating File Field
        if FileField.filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']:
            if not os.path.exists(current_app.root_path + ImageFolderPath):
                os.mkdir(current_app.root_path + ImageFolderPath)
            # Generating Unique ID For Image
            ImageID = uuid.uuid4()
            ImageID = str(ImageID)
            ImageID = ImageID.rsplit('-',1)
            ImageExt = FileField.filename.rsplit('.',1)[1]
            NewImageName = ImageName + ImageID[1] + '.' + ImageExt
            FileField.filename = NewImageName
            filename = secure_filename(FileField.filename)
            # Saving the image
            FileField.save(current_app.root_path + os.path.join(ImageFolderPath,filename))
            path =  ImageFolderPath[7:] + filename
            return path