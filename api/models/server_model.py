from database import DatabaseConnection

class ServidorDs:

    def __init__(self,**kwargs):
        self.id_servidor = kwargs.get('id_servidor')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.fecha_creacion = kwargs.get('fecha_creacion')

    def serialize(self):
        return {
            "id_servidor": self.id_servidor,
            "nombre_servidor": self.nombre_servidor,
            "fecha_creacion": self.fecha_creacion
        }
    
    @classmethod
    def creat_server(cls, nombre):
        conn = DatabaseConnection.get_connection()  
        query = "INSERT INTO servidores (nombre_servidor, fecha_creacion) VALUES (%s, CURRENT_TIMESTAMP)"
        params = (nombre,)  
        DatabaseConnection.execute_query(conn, query, params)  
        DatabaseConnection.close_connection(conn)  

    @classmethod
    def delete_sv(cls, id_sv):
        conn = DatabaseConnection.get_connection()  # Obtener la conexión
        qry = "DELETE FROM servidores WHERE id_servidor = %s"
        params = (id_sv,)  # Debe ser una tupla
        DatabaseConnection.execute_query(conn, qry, params)  # Pasar la conexión a execute_query
        DatabaseConnection.close_connection(conn)  # Cerrar la conexión
    
    @classmethod
    def sv_registered(cls, srver):
        qry = "SELECT * FROM servidores WHERE nombre_servidor = %s"
        params = (srver.nombre_servidor,)  
        conn = DatabaseConnection.get_connection()  
        result = DatabaseConnection.fetch_one(conn, qry, params=params) 
        DatabaseConnection.close_connection(conn) 

        if result is not None:
            return True
        return False

    @classmethod
    def get_sv(cls, nombre_servidor):
        qry = "SELECT id_servidor FROM servidores WHERE nombre_servidor = %s"
        params = (nombre_servidor,)  
        conn = DatabaseConnection.get_connection()  
        result = DatabaseConnection.fetch_one(conn, qry, params=params)  
        DatabaseConnection.close_connection(conn)  
    
    
