from ..models.server_model import ServidorDs
from flask import request, session


class ServerController:

    @classmethod
    def crear_sv(cls):
        data = request.json
        session['nombre_servidor'] = data.get('nombre_servidor')
        servidor = ServidorDs(data.get('nombre_servidor'))
        ServidorDs.creat_server(servidor)
        #Crear datos con tabla intermedia
        return {'msj':'Server creado'},201
    
    @classmethod
    def obtener_servers(cls):
        servers = ServidorDs.get_servidores()
        return servers
