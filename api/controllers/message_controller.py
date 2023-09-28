from models.message_model import Mensaje
from flask import request



class MessageController:

    @classmethod
    def ver_mensajes_ordenados_cronológicamente(cls, id_canal):
        channel = Mensaje(id_canal=id_canal)
        all_messages = Mensaje.ver_mensajes_ordenados_cronológicamente(channel)
        mensajes = []
        if all_messages is not None:
            for message in all_messages:
                mensajes.append(message.serialize())
            return mensajes, 200
        
    @classmethod
    def crear_mensaje(cls):
        data = request.json

        if data is not None:
            mensaje = Mensaje(**data)
            Mensaje.crear_mensaje(mensaje)
            return {'succes'},201
        
    @classmethod
    def modificar_mensaje(cls ,id_mensaje):
        data = request.json
        if data is not None:
            data['id_mensaje'] = id_mensaje
            msj = Mensaje(**data)
            Mensaje.modificar_mensaje(msj)
            return {'succes'},201
        
    @classmethod
    def eliminar_mensaje(cls, id_mensaje):
        data = request.json
        mensaje_a_borrar = Mensaje(id_mensaje = id_mensaje) 
        if data is not None:
            Mensaje.eliminar_mensaje(mensaje_a_borrar)
            return {'succes'},201










