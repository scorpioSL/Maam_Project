from app.database import UserLog
from flask_login import current_user

class UserLog:
    # Variable Defination
    Response = None
    action = None
    description = None

    # Constructor
    def __init__(self, action, description):
        self.User = current_user

    # Create Log
    def createLog(self, action, description):
        self.action = action
        self.description = description
        try:
            UserLog(User = self.User,Action = self.action,Description = self.description,Response = "Success",UserCreated = self.User).save()
        except Exception e:
            UserLog(User = current_user,Action = self.action,Description = self.description,Response = e,UserCreated = self.User).save()
            print(f"Something went wrong: {e}")
        finally:
            if e in None:
                print("The operation is successfully finished")
            else:
                print("Error!")

    def getallLogs(self):
        return UserLog.objects()
            

    
