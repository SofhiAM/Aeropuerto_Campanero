import sqlite3
from sqlite3 import Error
from .conexiones import conexion_db

#///////////////////////////Registrar Usuarios///////////////////////////////////////////////////////////////////
def registrar_usuario(datos):
    conn = conexion_db()
    sql = """INSERT INTO usuario 
            (id_usuario, tipo_id, nom_usuario, ape_usuario, correo_usu, contraseña_usu, tipo_cuenta) 
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    try:
        cursor = conn.cursor()
        cursor.execute (sql, datos)
        conn.commit()
        print("Nuevo usuario agregado")
        return True

    except Error as e:
        print ("Error al registrar usuario "+ str(e))

    finally:
        if conn:
            cursor.close()
            conn.close()
#---------------------------------------------------------------------------------------------------------------
def verificacioncontrasena(_correo):
    conn = conexion_db()
    sql = f"""SELECT contraseña_usu FROM usuario WHERE correo_usu = '{_correo}'"""

    try: 
        cur = conn.cursor()
        cur.execute (sql)
        contrasena = cur.fetchone()
        return contrasena

    except Error as e:
        print ("Error seleccionando contraseña: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
#---------------------------------------------------------------------------------------------------------------
def verificaciontipo(_correo):
    conn = conexion_db()
    sql = f"""SELECT tipo_cuenta FROM usuario WHERE correo_usu = '{_correo}'"""

    try: 
        cur = conn.cursor()
        cur.execute(sql)
        tipo = cur.fetchone()
        return tipo

    except Error as e:
        print ("Error seleccionando tipo: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
#---------------------------------------------------------------------------------------------------------------    
def traer_todoslos_usuarios ():
    
    con = conexion_db()

    sql = """SELECT id_usuario, tipo_id, nom_usuario, ape_usuario, correo_usu, tipo_cuenta FROM usuario order by 1;"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        usuario = cursor.fetchall()
        return usuario

    except Error as e:
        print ("Error al traer usuarios: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# ////////////////////////////// BORRAR USUARIO ////////////////////////////
def eliminar_id_usuario (_id_usuario):
    con = conexion_db()
    sql = f"DELETE FROM usuario WHERE id_usuario= '{_id_usuario}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Usuario Eliminado")
        return True

    except Error as e:
        print ("Error al eliminar el Usuario "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()


#**
# ////////////////////////////// MODIFICAR USUARIO ////////////////////////////
def buscar_usuario(_id_usuario):
    con = conexion_db()

    sql = f"""SELECT id_usuario, tipo_id, nom_usuario, ape_usuario, correo_usu, 
            contraseña_usu, tipo_cuenta FROM usuario WHERE id_usuario = {_id_usuario};"""

    try:
        cursor = con.cursor()
        cursor.execute (sql,_id_usuario)
        con.commit()
        usuario = cursor.fetchone()
        return usuario

    except Error as e:
        print ("Error al traer usuario: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
#------------------------------------------------------------------------------
def actualizar_usuario (_id_usuario, datos):
    conn = conexion_db()
    sql = f""" UPDATE usuario SET
                            id_usuario = %s,
                            tipo_id = %s,
                            nom_usuario = %s,
                            ape_usuario = %s,
                            correo_usu = %s,
                            contraseña_usu = %s,
                            tipo_cuenta = %s

            WHERE id_usuario = {_id_usuario}
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        print("Usuario Actualizado")
        return True

    except Error as e:
        print ("Error al actualizar usuario "+ str(e))

    finally:
        if conn:
            cursor.close()
            conn.close()

# --------------------------------------------------------------
def consultar_entidad (_contrasena):
    con = conexion_db()

    sql = f"""SELECT entidad from usuario where contraseña_usu = '{_contrasena}';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql,_contrasena)
        con.commit()
        entidad = cursor.fetchone()
        return entidad

    except Error as e:
        print ("Error al traer entidad: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()