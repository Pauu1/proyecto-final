import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON

render = web.template.render('mvc/view/admin', base="layout")

class Actualizar_sucursal:
    def GET(self, localId): 
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            sucursal = db.child("sucursales").child(localId).get()
            return render.actualizar_sucursal(sucursal)
        except Exception as error:  
            print("Error actualizar_sucursal.GET: {}".format(error))  
    

    def POST(self, localId):
        try:
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            db = firebase.database() 
            formulario = web.input() 
            name= formulario.name
            temperatura= formulario.temperatura
            humedad = formulario.humedad 
            email = formulario.email
            empresa = formulario.empresa
            data = {
                "name": name,
                "temperatura": temperatura,
                "humedad": humedad,
                "email": email,
                "empresa": empresa,
            }
            db.child("sucursales").child(localId).update(data)
            return web.seeother("/insertar_sucursal")
        except Exception as error:
            print("Error actualizar_sucursal update.GET: {}".format(error))