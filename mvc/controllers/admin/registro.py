import web
import pyrebase 
import firebase_config as token
import json

render = web.template.render('mvc/view/admin', base="layout")

class Registro:
    def GET(self): 
        try: 
            message = None 
            return render.registro(message) 
        except Exception as error: 
            message = "Error en el sistema" 
            print("Error registro.GET: {}") 
            return render.registro(message) 


    def POST(self): 
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database() 
            formulario = web.input() 
            name= formulario.name
            phone= formulario.phone
            email = formulario.email 
            password= formulario.password 

            user = auth.create_user_with_email_and_password(email,password)  
            local_id =  (user ['localId'])
            data = {
            "name": name,
            "phone": phone,
            "email": email,
            }
            results = db.child("users").child(user['localId']).set(data)
            return web.seeother("/bienvenida_administrador") 
        except Exception as error: 
            formato = json.loads(error.args[1]) # Error en formato JSON
            error = formato['error'] 
            message = error['message']
            print("Error Registro.POST: {}".format(message)) 
            web.setcookie('localID', None, 3600) 
            return render.registro(message) 