import web
import pyrebase 
import firebase_config as token
import json


render = web.template.render('mvc/view/operador', base="layout")


class Bienvenida_operador:
    def GET(self): 
        if ( web.cookies().get('localid')) != "": 
            return render.bienvenida_operador() 
        else:
            return render.login() 