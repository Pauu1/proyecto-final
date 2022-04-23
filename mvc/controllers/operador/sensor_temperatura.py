import web
import pyrebase 
import firebase_config as token
import json


render = web.template.render('mvc/view/operador', base="layout")


class Sensor_temperatura:
      def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            return render.sensor_temperatura() 
        except Exception as error: 
            print("Error sensor_temperatura.GET: {}".format(error))