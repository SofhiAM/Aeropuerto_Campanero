import sqlite3
from sqlite3 import Error
from .conexiones import conexion_db


def comprobar_id ():
    con = conexion_db()

    sql = """SELECT id_avion from avion"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        aviones = cursor.fetchall()
        return aviones

    except Error as e:
        print ("Error al traer cod aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------
def registrar_avion (datos):
    #avion = (cod_avion, tipo_avion, propulsion, modelo, capacidad, motores, peso)
    con = conexion_db()
    sql = """ INSERT INTO avion (id_avion, tipo_avion, capacidad, cod_modelo) VALUES (%s,%s,%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, datos)
        con.commit()
        print("Avion almacenado")
        return True

    except Error as e:
        print ("Error asignar hangar "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------
def buscar_cod_modelo (_descripcion):
    con = conexion_db()

    sql = f"""SELECT cod_modelo FROM modelo WHERE descripcion = '{_descripcion}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        cod_modelo = cursor.fetchone()
        return cod_modelo

    except Error as e:
        print ("Error al traer cod aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------------------------------
def traer_modelos ():
    con = conexion_db()
    sql = """ SELECT descripcion from modelo"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        modelos = cursor.fetchall()
        return modelos

    except Error as e:
        print ("Error al traer modelos de aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# -------------------------------------------------------------------------------------
def buscar_modelo (_id_avion):
    con = conexion_db()

    sql = f"""SELECT descripcion FROM modelo join avion on modelo.cod_modelo = avion.cod_modelo 
            WHERE avion.id_avion = '{_id_avion}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        modelo = cursor.fetchone()
        return modelo

    except Error as e:
        print ("Error al traer cod aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------------------------------
def buscar_avion(_id_avion):
    con = conexion_db()

    sql = f"""SELECT id_avion, tipo_avion, capacidad, avion.cod_modelo, tipo_propulsion, peso_nominal,
            num_motores, descripcion FROM avion join modelo on avion.cod_modelo = modelo.cod_modelo 
            WHERE id_avion = '{_id_avion}';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        avion = cursor.fetchone()
        return avion

    except Error as e:
        print ("Error al traer avion: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
#------------------------------------------------------------------------------
def consulta_por_modelo(_descripcion):
    con = conexion_db()

    sql = f"""SELECT tipo_propulsion, peso_nominal, num_motores FROM modelo WHERE descripcion = '{_descripcion}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        modelo = cursor.fetchone()
        print(modelo)
        return modelo

    except Error as e:
        print ("Error al traer modelo: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
#------------------------------------------------------------------------------
def actualizar_avion (_id_avion, datos):
    conn = conexion_db()
    sql = f""" UPDATE avion SET
                            id_avion = %s,
                            tipo_avion = %s,
                            capacidad = %s
                            
            WHERE id_avion = '{_id_avion}'
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        print("Avion Actualizado")
        return True

    except Error as e:
        print ("Error al actualizar avion "+ str(e))

    finally:
        if conn:
            cursor.close()
            conn.close()

# ////////////////////////////// BORRAR AVION ////////////////////////////
def eliminar_id_avion (_id_avion):
    con = conexion_db()
    sql = f"DELETE FROM avion WHERE id_avion= '{_id_avion}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Avion Eliminado")
        return True

    except Error as e:
        print ("Error al eliminar el Avion "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

def traer_aviones ():
    con = conexion_db()

    sql = """SELECT id_avion, tipo_avion, descripcion, tipo_propulsion, capacidad, peso_nominal, num_motores
            FROM avion join modelo on avion.cod_modelo = modelo.cod_modelo"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        aviones = cursor.fetchall()
        return aviones

    except Error as e:
        print ("Error al traer aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

def borrar_datos_avion (_id_avion):
    con = conexion_db()
    sql = f"DELETE FROM avion WHERE id_avion= '{_id_avion}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Avion eliminado.")
        return True

    except Error as e:
        print ("Error al eliminar avion "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()