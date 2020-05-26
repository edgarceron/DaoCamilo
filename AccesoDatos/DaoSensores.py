from .Logica.Sensores import Sensores

class DaoSensores:
    def __init__(self, conexion):
        self.conexion = conexion

    def guardarSensores(self, sensores):
        sql_guardar = "INSERT INTO sensores (lugar, tipo, numero_serie, t_int, numero_capt, mision_id) VALUES "
        sql_guardar += "('" + sensores.lugar + "', '" + sensores.tipo + "', '" + sensores.numero_serie + "', " 
        sql_guardar += str(sensores.t_int) + "," + str(sensores.numero_capt) + ", "
        sql_guardar += str(sensores.mision_id) + ") RETURNING *"

        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            result = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            sensores.id = result[0]
            print(result)
            return sensores
            
        except(Exception) as e:
            print("Error al insertar registro", e)
            return None


    def actualizarSensores(self, sensores):
        sql_guardar = "UPDATE sensores SET" 
        sql_guardar += " lugar = '" + sensores.lugar + "', tipo = " + str(sensores.tipo) 
        sql_guardar += ", numero_serie = " + str(sensores.numero_serie) 
        sql_guardar += ", t_int = '" + sensores.t_int + "', numero_capt = '" + sensores.numero_capt + "', "
        sql_guardar += "mision_id = " + str(sensores.mision_id) + " WHERE id = " + str(sensores.id)
        sql_guardar += " RETURNING *"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            result = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            return sensores
            
        except(Exception) as e:
            print("Error al actualizar el sensores", e)
            return None


    def borrarSensores(self, sensores):
        sql_borrar = "DELETE FROM sensores WHERE id = " + str(sensores.id) + ";"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_borrar)
            
        except(Exception) as e:
            print("Error al actualizar la sensores", e)
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")

    def getSensores(self, id_sensores):
        sql_select = "SELECT * FROM sensores WHERE id = " + str(id_sensores)
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_select)
            record = cursor.fetchone()
            result = Sensores()
            result.id = record[0]
            result.lugar = record[1]
            result.tipo	 = record[2]
            result.numero_serie = record[3]
            result.t_int = record[4]
            result.numero_capt = record[5]
            result.mision_id = record[6]
            return result

        except(Exception) as e:
            print("Error al actualizar el usuario", e)
            result = None
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")
            return result
