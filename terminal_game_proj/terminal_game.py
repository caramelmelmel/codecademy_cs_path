import pyrebase
from firebase_config import config

firebase = pyrebase.initialize_app(config)

# use the auth feature for multiplayer
auth = firebase.auth()

def user_in_db():
    email = input("Welcome to the new game of wonder! start by shouting your email!")
    password = input("what's your password")
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("seems good! you are in the database!")
    except:
        print("seems like we are unable to find you in the database... let me register you")
        auth.create_user_with_email_and_password(email,password)
        print("we have created your email and password")

class wizard:
    def __init__(self):
        self.attack = 5


