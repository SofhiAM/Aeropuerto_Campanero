from .conexiones import conexion_db
from psycopg2 import Error

def traer_todos_hangares ():
    
    con = conexion_db()

    sql = """SELECT cod_hangar, estado_hg FROM hangar order by 1;"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        hangares = cursor.fetchall()
        return hangares

    except Error as e:
        print ("Error al traer hangares: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# ------------------------------------------------------------
def traer_todas_aerolineas ():
    
    con = conexion_db()
    sql = """SELECT nom_aerolinea from aerolinea"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        aerolineas = cursor.fetchall()
        return aerolineas

    except Error as e:
        print ("Error al traer aerolineas: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------
def alquilar_hangar(datos):
    print(datos[0])

    con = conexion_db()
    sql = """ INSERT INTO alquiler (cod_hangar, id_avion, fecha_alquiler, 
            hora_alquiler, costo_base, aero_dueña) VALUES (%s,%s,%s,%s,%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, datos)
        con.commit()
        print("Hangar alquilado")
        return True

    except Error as e:
        print ("Error asignar hangar "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

#--------------------------------------------------------------------------------
def consultar_estado_hangar (_cod_hangar):
    
    con = conexion_db()
    sql = f" SELECT estado_hg FROM hangar WHERE cod_hangar = '{_cod_hangar}' "

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        hangar = cursor.fetchone()
        return hangar

    except Error as e:
        print ("Error al traer estado: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------
def cambiar_estado_alibre (cod_hangar):

    con = conexion_db()
    sql = f"UPDATE hangar SET estado_hg = 'LIBRE' WHERE cod_hangar = '{_cod_hangar}' "

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Cambio de estado = Libre")
        return True

    except Error as e:
        print ("Error cambio estado "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------------------------------
def cambiar_estado_aocupado (_cod_hangar):

    con = conexion_db()
    sql = f"UPDATE hangar SET estado_hg = 'OCUPADO' WHERE cod_hangar = '{_cod_hangar}' "

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Cambio de estado = Ocupado")
        return True

    except Error as e:
        print ("Error cambio estado "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ----------------------------------------------------------------------------------------
def datos_factura (_cod_hangar):
    con = conexion_db()
    sql = f"""SELECT descripcion, aero_dueña, hora_alquiler, fecha_alquiler, costo_base 
            FROM alquiler join avion on alquiler.id_avion = avion.id_avion join modelo on avion.cod_modelo = modelo.cod_modelo 
            WHERE cod_hangar = '{_cod_hangar}' """

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        datos = cursor.fetchone()
        print(datos)
        return datos

    except Error as e:
        print ("Error al traer estado: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------------------------------------
def generar_salida (_cod_hangar):
    con = conexion_db()
    sql = f"DELETE FROM alquiler WHERE cod_hangar= '{_cod_hangar}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Salida generada.")
        return True

    except Error as e:
        print ("Error al generar la salida "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------------------
def cambiar_estado_alibre (_cod_hangar):

    con = conexion_db()
    sql = f"UPDATE hangar SET estado_hg = 'LIBRE' WHERE cod_hangar = '{_cod_hangar}' "

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Cambio de estado = Libre")
        return True

    except Error as e:
        print ("Error cambio estado "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()