import web
import pyrebase 
import firebase_config as token
import json

 
render = web.template.render('mvc/view/public', base="layout")


class R_contraseña:
    def GET(self): 
           return render.r_contraseña() 

    def POST(self): 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            formulario = web.input() 
            email = formulario.email
            results = auth.send_password_reset_email(email)
            print(results)
            return web.seeother("/login")