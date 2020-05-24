from .Logica.Espectros import Espectros

class DaoEspectros:
    def __init__(self, conexion):
        self.conexion = conexion

    def guardarEspectros(self, espectros):
        sql_guardar = "INSERT INTO espectros (nombre, elevacion, velocidad, modo_vuelo, modo_adq, usuarios_id) VALUES "
        sql_guardar += "('" + espectros.nombre + "', " + str(espectros.elevacion) + ", " + str(espectros.velocidad) + ", '" 
        sql_guardar +=  espectros.modo_vuelo + "','" + espectros.modo_adq + "', "
        sql_guardar += str(espectros.usuarios_id) + ") RETURNING *"

        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            result = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            espectros.id = result[0]
            return espectros
            
        except(Exception) as e:
            print("Error al insertar registro", e)
            return None


    def actualizarEspectros(self, espectros):
        sql_guardar = "UPDATE espectros SET" 
        sql_guardar += " nombre = '" + espectros.nombre + "', elevacion = " + str(espectros.elevacion) 
        sql_guardar += ", velocidad = " + str(espectros.velocidad) 
        sql_guardar += ", modo_vuelo = '" + espectros.modo_vuelo + "', modo_adq = '" + espectros.modo_adq + "', "
        sql_guardar += "usuarios_id = " + str(espectros.usuarios_id) + " WHERE id = " + str(espectros.id)
        sql_guardar += " RETURNING *"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            result = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            return espectros
            
        except(Exception) as e:
            print("Error al actualizar el espectros", e)
            return None


    def borrarEspectros(self, espectros):
        sql_borrar = "DELETE FROM espectros WHERE id = " + str(espectros.id) + ";"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_borrar)
            
        except(Exception) as e:
            print("Error al actualizar la espectros", e)
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")

    def getEspectros(self, id_espectros):
        sql_select = "SELECT * FROM espectros WHERE id = " + str(id_espectros)
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_select)
            record = cursor.fetchone()
            result = Espectros()
            result.id = record[0]
            result.nombre = record[1]
            result.elevacion = record[2]
            result.velocidad = record[3]
            result.modo_vuelo = record[4]
            result.modo_adq = record[5]
            result.usuarios_id = record[6]
            return result

        except(Exception) as e:
            print("Error al actualizar el usuario", e)
            result = None
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")
            return result
