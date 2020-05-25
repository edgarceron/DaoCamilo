from .Logica.Espectros import Espectros

class DaoEspectros:
    def __init__(self, conexion):
        self.conexion = conexion

    def guardarEspectros(self, espectros):
        sql_guardar = "INSERT INTO espectros (white, dark, capturado, resultado, sensores_id) VALUES "
        sql_guardar += "(%s, %s, %s, %s, %s) RETURNING *"

        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                sql_guardar, 
                (
                    espectros.white, espectros.dark, espectros.capturado, 
                    espectros.resultado,espectros.sensores_id 
                ) 
            )
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
        sql_guardar += "white = %s, dark = %s, capturado = %s, resultado = %s, "
        sql_guardar += "sensores_id = %s"

        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                sql_guardar,
                (
                    espectros.white,
                    espectros.dark,
                    espectros.capturado,
                    espectros.resultado,
                    espectros.sensores_id
                )
            )
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
            result.white = record[1]
            result.capturado = record[2]
            result.resultado = record[3]
            result.sensores_id = record[4]
            return result

        except(Exception) as e:
            print("Error al actualizar el usuario", e)
            result = None
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")
            return result
