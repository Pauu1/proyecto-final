import web
import pyrebase 
import firebase_config as token
import json 

render = web.template.render('mvc/view/public', base="layout")

class Inicio:
    def GET(self):
        return render.inicio()