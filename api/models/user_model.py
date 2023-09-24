from database import DatabaseConnection

class User:

    def __init__(self, **kwargs):
        self.id_usuario = kwargs.get('id_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido  = kwargs.get('apellido ')
        self.username = kwargs.get('username')
        self.paswwordd = kwargs.get('paswwordd')
        self.email = kwargs.get('email')
        self.estado  = kwargs.get('estado')
        self.rol  = kwargs.get('rol')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
    
    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido ": self.apellido,
            "username": self.username,
            "paswwordd": self.paswwordd,
            "email": self.email,
            "estado" : self.estado,
            "rol" : self.rol,
            "fecha_nacimiento": self.fecha_nacimiento
        }

    @classmethod
    def is_registered(cls, user):
        query = """SELECT id_usuario FROM discord_db.usuarios 
        WHERE username = %(username)s and passwordd = %(paswword)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = """SELECT * FROM authentication_db.users 
        WHERE username = %(username)s"""
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_usuario = result[0],
                nombre = result[1],
                apellido = result[2],
                username = result[3],
                paswword = result[4],
                email = result[5],
                estado_usuario = result[6],
                rol_usuario = result[7],
                fecha_nacimiento = result[8])
        return None
    
    @classmethod
    def crear_usuario(cls, nombre, apellido, username, passwordd, email, estado_usuario, rol_usuario, fecha_nacimiento):
        query = "INSERT INTO usuarios (nombre, apellido, username, paswwordd, email, estado_usuario, rol_usuario, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        params = (nombre, apellido, username, passwordd, email, estado_usuario, rol_usuario, fecha_nacimiento)
        cursor = DatabaseConnection.execute_query(query, params=params)
        cursor.close()

    @classmethod
    def modificar_usuario(cls, id_usuario, nombre, apellido, username, passwordd, email, estado_usuario, rol_usuario):
        query = "UPDATE usuarios SET nombre = %s, apellido = %s, username = %s, passwordd = %s, email = %s, estado_usuario = %s, rol_usuario = %s WHERE id_usuario = %s"
        params = (nombre, apellido, username, passwordd, email, estado_usuario, rol_usuario, id_usuario)
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
