import json
import os
import uuid


FILE_NAME = "user.json"


# File check aur load karna
def load_user():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME) as f:
            return json.load(f)
        return []
    

# File mein data save karna
def Save_user(user):
    with open(FILE_NAME , "w") as f :
        json.dump(user , f , indent=4)


# SignUp function
def signup():
    users = load_user()
    email = input(" Enter your email: ")

     # Duplicate email check
    for user in users:
        if user["email"] == email:
            print("⚠️ Email already registered!")
            return
        


name = input(" Enter your name :")
age  = input(" Enter your age : ")
country = input(" Enter your Country : ")
password = input(" Create your password: ")



user_id = str(uuid.uuid4())


new_user = {
    "id" : user_id,
    "name" : name,
    "age" : age,
    "country" : country ,
    "email" : email ,
  }




  
    

 



