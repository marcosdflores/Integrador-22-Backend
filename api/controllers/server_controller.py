from models.server_model import ServidorDs
from flask import templates , request, session


class ServerController:

    @classmethod
    def crear_sv(cls):
        data = request.json
        session['nombre_servidor'] = data.get('nombre_servidor')
        servidor = ServidorDs(**data)
        if not ServidorDs.sv_registered(servidor):
            ServidorDs.creat_server(servidor)
            sv = ServidorDs.get_sv()
            #Crear datos con tabla intermedia
            return {'msj':'Server creado'},201
        return {'msj':'Ocurrio un error'},400