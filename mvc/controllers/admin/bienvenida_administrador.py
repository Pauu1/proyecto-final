import web
import pyrebase 
import firebase_config as token
import json

render = web.template.render('mvc/view/admin', base="layout")


class Bienvenida_administrador:
    def GET(self): 
        if ( web.cookies().get('localid')) != "": 
            return render.bienvenida_administrador()
        else:
            return render.login() 