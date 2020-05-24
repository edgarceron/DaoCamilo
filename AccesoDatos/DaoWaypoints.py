from .Logica.Waypoints import Waypoints

class DaoWaypoints:
    def __init__(self, conexion):
        self.conexion = conexion

    def guardarWaypoint(self, waypoint):
        sql_guardar = "INSERT INTO waypoints (num_waypoint, latlon, mision_id) VALUES "
        sql_guardar += "(" + str(waypoint.num_waypoint) + ", '" + waypoint.latlon + "',"
        sql_guardar += str(waypoint.mision_id) + ") RETURNING *;"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            result = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            print("Registro guardado con exito")
            waypoint.id = result[0]
            return waypoint 
            
        except(Exception) as e:
            print("Error al insertar registro", e)
            return None

    def actualizarWaypoint(self, waypoint):
        sql_guardar = "UPDATE waypoints SET num_waypoint = " + str(waypoint.num_waypoint) 
        sql_guardar += ", latlon = '" + waypoint.latlon + "', mision_id = " + str(waypoint.mision_id) 
        sql_guardar += " WHERE id = " + str(waypoint.id) + ";"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_guardar)
            self.conexion.commit()
            cursor.close()
            return waypoint
            
        except(Exception) as e:
            print("Error al actualizar el waypoint", e)
            return None

    def borrarWaypoint(self, waypoint):
        sql_borrar = "DELETE FROM waypoints WHERE id = " + str(waypoint.id) + ";"
        
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_borrar)
            self.conexion.commit()
            cursor.close()
            
        except(Exception) as e:
            print("Error al actualizar el waypoint", e)


    def getWaypoint(self, id_waypoint):
        sql_select = "SELECT * FROM waypoints WHERE id = " + str(id_usuario)
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql_select)
            record = cursor.fetchone()
            result = Usuarios.Usuarios()
            result.id = record[0]
            result.nombre = record[1]
            result.contrasena = record[2]
            cursor.close()
            return result

        except(Exception) as e:
            print("Error al actualizar el usuario", e)
            result = None
        
        finally:
            if(cursor):
                cursor.close()
                print("Se ha cerrado el cursor")
            return result
