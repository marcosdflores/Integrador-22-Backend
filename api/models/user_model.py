from ..database import DatabaseConnection

class User:

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.username = kwargs.get('username')
        self.paswwordd = kwargs.get('paswwordd')
        self.email = kwargs.get('email')
        self.imagen = kwargs.get("imagen")
        self.estado = kwargs.get('estado')
        self.rol = kwargs.get('rol')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "username": self.username,
            "paswwordd": self.paswwordd,
            "email": self.email,
            "imagen": self.imagen,
            "estado" : self.estado,
            "rol" : self.rol,
            "fecha_nacimiento": self.fecha_nacimiento
        }

    @classmethod
    def is_registered(cls, user):
        query = """SELECT id_usuario FROM discord_db.usuarios 
        WHERE username = %(username)s and passwordd = %(paswwordd)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get_user(cls, user):
        query = """SELECT * FROM discord_db.users 
        WHERE username = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                nombre = result[1],
                apellido = result[2],
                username = result[3],
                paswwordd = result[4],
                email = result[5],
                imagen = result[6]
                estado_usuario = result[7],
                rol_usuario = result[8],
                fecha_nacimiento = result[9])
        return None
    
    @classmethod
    def crear_usuario(cls, user):
        query = "INSERT INTO discord_db.usuarios (nombre, apellido, username, paswwordd, email, imagen, fecha_nacimiento,) VALUES (%(nombre)s, %(apellido)s, %(username)s, %(paswwordd)s, %(email)s, %(imagen)s, %(fecha_nacimiento)s);"
        params = user.__dict__
        DatabaseConnection.execute_query(query, params=params)


    @classmethod
    def modificar_usuario(cls, id_usuario, nombre, apellido, username, passwordd, email, imagen_url):
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, username = %s, passwordd = %s, email = %s, imagen = %s WHERE id_usuario = %s"
        params = (nombre, apellido, username, passwordd, email, imagen_url, id_usuario)
        cursor = DatabaseConnection.execute_query(query, params=params)
        cursor.close()

    @classmethod
    def eliminar_usuario(cls, id_usuario):
        query = "DELETE FROM usuarios WHERE id_usuario = %s"
        params = (id_usuario,)
        cursor = DatabaseConnection.execute_query(query, params=params)
        cursor.close()

    @classmethod
    def ver_usuario(cls, id_usuario):
        query = "SELECT * FROM usuarios WHERE id_usuario = %s"
        params = (id_usuario,)
        cursor = DatabaseConnection.fetch_one(query, params=params)
        if cursor:
            return cls(*cursor)
        return None
