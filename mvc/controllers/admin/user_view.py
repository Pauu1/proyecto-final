import web
import pyrebase 
import firebase_config as token
import json


render = web.template.render('mvc/view/admin', base="layout")


class User_view:                             
    def GET(self,localId):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            user =  db.child("users").child(localId).get()
            return render.user_view(user) 
        except Exception as error: 
            message = "Error en el sistema"
            print("Error Login.GET: {}".format(error))