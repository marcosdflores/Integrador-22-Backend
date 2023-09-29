from ..models.user_model import User
from flask import request, session
from models.exceptions import BadRequestError, NotFoundError, ForbiddenError, ServerError



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
            raise BadRequestError("Usuario o contraseña incorrectos"), 400
            

    @classmethod
    def show_profile(cls):
        username = session.get('username')
        user = User.get_user(User(username = username))
        if user is None:
            raise NotFoundError("Usuario no encontrado"), 404
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
        return ('Usuario creado con éxito'), 200
    
    def modificar_usuario(id_usuario):
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
                    data_actualizada.get("passwordd", data_original.passwordd),
                    data_actualizada.get("email", data_original.email),
                    data_actualizada.get("imagen_url", data_original.imagen),
                ) 
    
    def eliminar_usuario(id_usuario):
        usuario = User.ver_usuario(id_usuario)
        if usuario and usuario.id_usuario == session.get('id_usuario'):
            User.eliminar_usuario(id_usuario)
            return('Usuario eliminado con éxito'),200
        else:
            raise ForbiddenError("No tienes permisos para realizar esta acción"),403
