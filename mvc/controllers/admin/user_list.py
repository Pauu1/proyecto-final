import web
import pyrebase 
import firebase_config as token
import json

render = web.template.render('mvc/view/admin', base="layout")

class User_list:                             
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            users = db.child("users").get()
            return render.user_list(users) 
        except Exception as error: 
            print("Error Login.GET: {}".format(error))