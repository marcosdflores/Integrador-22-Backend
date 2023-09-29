from ..models.user_model import User
from flask import request, session



class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            username = data.get('username'),
            paswwordd = data.get('paswwordd')
        )
        
        if User.is_registered(user):
            session['username'] = data.get('username')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401

            
    @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get_user(User(username = username))
        if user is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return user.serialize(), 200
    
    @classmethod
    def logout(cls):
        session.pop('username', None)
        return {"message": "Sesion cerrada"}, 200
    
    @classmethod
    def crear_usuario(cls):
        data_user = request.json

        nuevo_user = User(**data_user)

        User.crear_usuario(nuevo_user)
        return ('Usuario creado con éxito'), 201
    
    @classmethod
    def modificar_usuario(cls, id_usuario):
        if 'username' in session:
            user = User(username = session['username'])
            user_encontrado = User.get_user(user)

            if user_encontrado and user_encontrado.id_usuario == id_usuario:
                data_actualizada = request.json
                data_original = user_encontrado

                # Lógica para manejar la imagen
                if 'imagen_url' in data_actualizada:
                    # Si esta entre la data, se actualiza la URL de la imagen en los datos del usuario
                    user_encontrado.imagen = data_actualizada['imagen_url']

                User.modificar_usuario(
                    id_usuario,
                    data_actualizada.get("nombre", data_original.nombre),
                    data_actualizada.get("apellido", data_original.apellido),
                    data_actualizada.get("username", data_original.username),
                    data_actualizada.get("paswwordd", data_original.paswwordd),
                    data_actualizada.get("email", data_original.email),
                    data_actualizada.get("imagen_url", data_original.imagen),
                ) 
                return {"message": "Usuario modificado exitosamente"}, 200
        return {"message": "No tienes permiso para modificar este usuario"}, 401
    
    @classmethod
    def eliminar_usuario(cls, id_usuario):
        usuario = User.ver_usuario(id_usuario)
        if usuario and usuario.id_usuario == session.get('id_usuario'):
            User.eliminar_usuario(id_usuario)
            return('Usuario eliminado con éxito'),200
        else:
            return('No tienes permiso para eliminar este usuario'), 401
