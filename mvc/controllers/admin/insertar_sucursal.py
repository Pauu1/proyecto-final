import web # libreria para usar el framework web.py
import pyrebase # libreria para contecarse con firebase
import firebase_config as token # archivo con la configuracion de firebase
import json # libreria para manejar el formato JSON

render = web.template.render('mvc/view/admin', base="layout_2")

class Insertar_sucursal:
    def GET(self): 
        try: 
            message = None 
            return render.insertar_sucursal(message) 
        except Exception as error: 
            message = "Error en el sistema" 
            print("Error insertar_sucursal.GET: {}") 
            return render.insertar_sucursal(message) 
    

    def POST(self): 
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database() 
            formulario = web.input() 
            name= formulario.name
            temperatura= formulario.temperatura
            humedad = formulario.humedad 
            email = formulario.email 
            password = formulario.password 
            empresa = formulario.empresa
            user = auth.create_user_with_email_and_password(email,password)  
            local_id =  (user ['localId'])
            data = {
            "name": name,
            "email": email,
            "temperatura": temperatura,
            "humedad": humedad,
            "empresa": empresa,
            }
            results = db.child("sucursales").child(user['localId']).set(data)
            return web.seeother("/bienvenida_administrador") 
        except Exception as error: 
            formato = json.loads(error.args[1]) 
            error = formato['error'] 
            message = error['message']
            return render.registro(message) 