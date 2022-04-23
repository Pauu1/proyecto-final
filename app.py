import web
import pyrebase 
import firebase_config as token
import json

urls = (
    '/', 'mvc.controllers.public.inicio.Inicio',  
    '/user_list', 'mvc.controllers.admin.user_list.User_list',
    '/bienvenida_administrador','mvc.controllers.admin.bienvenida_administrador.Bienvenida_administrador',
    '/sensor_temperatura','mvc.controllers.admin.sensor_temperatura.Sensor_temperatura', 
    '/user_view/(.*)','mvc.controllers.admin.user_view.User_view',
    '/sensor','mvc.controllers.operador.sensor.Sensor',
    '/login', 'mvc.controllers.public.login.Login',
     '/registro','mvc.controllers.admin.registro.Registro',
    '/bienvenida_operador','mvc.controllers.operador.bienvenida_operador.Bienvenida_operador',
    '/r_contraseña', 'mvc.controllers.public.r_contraseña.R_contraseña',   
)
app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = False 
    app.run()