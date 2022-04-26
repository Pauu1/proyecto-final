import web # se importa la libreria de web.py para hacer sus del framework
import pyrebase # se importa la libreria de firebase para hacer uso de la fire base creada de google
import firebase_config as token # se importa la libreria de firebase_comfig para hacer uso de nuestro token de fire base
import json # se importa la libreria de json para hacer uso y modificación de estos elementos


render = web.template.render('mvc/view/admin', base="layout")

class sucursales:                             
    def GET(self):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            users = db.child("sucursales").get()
            return render.sucursales(users) 
        except Exception as error: 
            print("Error Login.GET: {}".format(error))