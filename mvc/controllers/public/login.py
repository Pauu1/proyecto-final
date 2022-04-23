import web
import pyrebase 
import firebase_config as token
import json

render = web.template.render('mvc/view/public', base="layout")
  
class Login: 
    def GET(self): 
        try: 
            message = None 
            return render.login(message)
        except Exception as error: # error
            message = "Error en el sistema" 
            print("Error Login.GET: {}".format(error))
            return render.login(message) 

    def POST(self): 
        try: 
            firebase = pyrebase.initialize_app(token.firebaseConfig) 
            auth = firebase.auth() 
            db = firebase.database()
            formulario = web.input() 
            email = formulario.email 
            password= formulario.password 
            nivel= formulario.nivel
            print(email,password) 
            user = auth.sign_in_with_email_and_password(email, password) 
            local_id =  (user ['localId'])
            print(local_id) 
            web.setcookie('localid', local_id)
            us =  db.child("users").child(user['localId']).get()
            if us.val()['nivel'] == 'administrador':
                return web.seeother("/bienvenida_administrador")
            else:
                return web.seeother("/bienvenida_operador")
        except Exception as error: # Error en formato JSON
            formato = json.loads(error.args[1])
            error = formato['error'] 
            message = error['message']
            if message == "invalid_password" :
                return render.login(message) 
            print("Error Login.POST: {}".format(message)) 
