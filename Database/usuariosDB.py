import sqlite3
from sqlite3 import Error
from .conexiones import create_connection

def verificacioncontraseña(correo):
    conn = create_connection()
    sql = f"""SELECT contraseña FROM Usuarios WHERE correo LIKE '%{correo}%'"""

    try: 
        cur = conn.cursor()
        cur.execute (sql)
        contraseña = cur.fetchall()
        return contraseña

    except Error as e:
        print ("Error seleccionando contraseña: "+ str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()

def verificaciontipo(_correo):
    conn = create_connection()
    sql = f"""SELECT tipo_usuario FROM Usuarios WHERE correo = {_correo}"""

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
    
