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
            "descripcion_canal ": self.descripcion_canal,
            "fecha_creacion ": self.fecha_creacion

        }
    
    @classmethod
    def crea_canal(cls, nombre, descrp):
        DatabaseConnection.get_connection()
        query = 'INSERT INTO canales (nombre_canal, descripcion_canal, fecha_creacion) VALUES (%s,%s, CURRENT_TIMESTAMP)'
        pmts = (nombre, descrp)
        DatabaseConnection.execute_query(query, pmts)
        DatabaseConnection.close_connection()

    @classmethod
    def get_canal(cls, id_canal):
        DatabaseConnection.get_connection()
        qry = 'SELECT * FROM canales WHERE id_canal = %s'
        DatabaseConnection.execute_query(qry, id_canal)
        DatabaseConnection.close_connection()


    @classmethod
    def verify_canal(cls, nombre):
        estado = True
        
        return estado
    
    #Revisar
