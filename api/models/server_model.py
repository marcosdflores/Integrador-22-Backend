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
            "fecha_creacion ": self.fecha_creacion
        }
    
    @classmethod
    def creat_server(cls, nombre):
        DatabaseConnection.get_connection()
        query = "INSERT INTO servidores (nombre_servidor, fecha_creacion) VALUES (%s, CURRENT_TIMESTAMP)"
        pmts = (nombre)
        DatabaseConnection.execute_query(query, pmts)
        DatabaseConnection.close_connection()
    
    @classmethod
    def delete_sv(cls, id_sv):
        DatabaseConnection.get_connection()
        qry = "DELETE FROM servidores WHERE id_servidor = %s"
        parameters = (id_sv,)
        DatabaseConnection.execute_query(qry, parameters)
        DatabaseConnection.close_connection()
    
    @classmethod
    def sv_registered(cls, srver):
        qry = """SELECT * FROM discord_db.servidores 
        WHERE nombre_servidor = %(nombre_servidor)s"""
        parametros = srver.__dict__
        DatabaseConnection.get_connection()
        resultad = DatabaseConnection.fetch_one(qry, params=parametros)
        DatabaseConnection.close_connection()

        if resultad is not None:
            return True
        return False

    def get_sv(cls, nombre_servidor):
        qry = """SELECT id_servidor FROM discord_db.servidores 
        WHERE nombre_servidor = %s"""
        DatabaseConnection.get_connection()
        resultad = DatabaseConnection.fetch_one(qry, params=nombre_servidor)
        DatabaseConnection.close_connection()

        #Revisar get_sv