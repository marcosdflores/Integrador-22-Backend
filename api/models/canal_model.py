from database import DatabaseConnection

class Canal:

    def __init__(self,**kwargs):
        self.id_canal = kwargs.get('id_canal')
        self.nombre_canal = kwargs.get('nombre_canal')
        self.descripcion_canal = kwargs.get('descripcion_canal')
        self.fecha_creacion = kwargs.get('fecha_creacion')

    def serialize(self):
        return {
            "id_canal": self.id_canal,
            "nombre_canal": self.nombre_canal,
            "descripcion_canal": self.descripcion_canal,
            "fecha_creacion": self.fecha_creacion

        }
    
    @classmethod
    def crea_canal(cls, nombre, descrp):
        conn = DatabaseConnection.get_connection()  
        query = 'INSERT INTO canales (nombre_canal, descripcion_canal, fecha_creacion) VALUES (%s, %s, CURRENT_TIMESTAMP)'
        pmts = (nombre, descrp)  
        DatabaseConnection.execute_query(conn, query, pmts)  
        DatabaseConnection.close_connection(conn)

    @classmethod
    def get_canal(cls, id_canal):
        conn = DatabaseConnection.get_connection()  
        qry = 'SELECT * FROM canales WHERE id_canal = %s'
        params = (id_canal,)  
        result = DatabaseConnection.execute_query(conn, qry, params) 
        DatabaseConnection.close_connection(conn)  



    @classmethod
    def verify_canal(cls, nombre):
        conn = DatabaseConnection.get_connection()  
        qry = 'SELECT COUNT(*) FROM canales WHERE nombre_canal = %s'
        params = (nombre,)  
        result = DatabaseConnection.execute_query(conn, qry, params) 
        DatabaseConnection.close_connection(conn)  

        
        if result[0][0] > 0:
            return True
        return False
