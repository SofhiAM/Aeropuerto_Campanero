from .conexiones import conexion_db
from psycopg2 import Error


#/////////////////////////////// REGISTRAR AEROLINEA CON TEL Y CORREO //////////////////////////////////
def registrar_aerolinea(datos):
    con = conexion_db()
    
    sql = """INSERT INTO aerolinea (nit_aerolinea, nom_aerolinea) VALUES (%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, datos)
        con.commit()
        print("Nueva aerolinea agregada")
        return True

    except Error as e:
        print ("Error al crear aerolinea "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------
def aerolinea_correo (datos):
    con = conexion_db()
    
    corsql = """INSERT INTO cor_aerolinea (nit_aerolinea, correo_aerolinea) VALUES (%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (corsql, datos)
        con.commit()
        print("Correo agregado")
        return True

    except Error as e:
        print ("Error al insertar correo "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------
def aerolinea_tel (datos):
    con = conexion_db()
    
    telsql = """INSERT INTO tel_aerolinea (nit_aerolinea, telef_aerolinea) VALUES (%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (telsql, datos)
        con.commit()
        print("Telefono agregado")
        return True

    except Error as e:
        print ("Error al insertar telefono "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ////////////////////////////// TRAER TODAS LAS AEROLÍNEAS AL MAIN PRINCIPAL ////////////////////////////
def seleccionar_todas_aerolineas ():
    con = conexion_db()

    sql = """ SELECT aerolinea.nit_aerolinea, nom_aerolinea, correo_aerolinea, telef_aerolinea 
                FROM (aerolinea CROSS JOIN cor_aerolinea) CROSS JOIN tel_aerolinea
                WHERE aerolinea.nit_aerolinea = cor_aerolinea.nit_aerolinea and
                aerolinea.nit_aerolinea = tel_aerolinea.nit_aerolinea"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        aerolineas = cursor.fetchall()
        print(aerolineas)
        return aerolineas

    except Error as e:
        print ("Error al seleccionar aerolineas: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ////////////////////////////// BORRAR AEROLINEA ////////////////////////////
def eliminar_aerolinea (_nit_aerolinea):
    con = conexion_db()
    sql = f"DELETE FROM aerolinea WHERE nit_aerolinea= '{_nit_aerolinea}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Aerolinea Eliminada")
        return True

    except Error as e:
        print ("Error al eliminar aerolinea "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

#------------------------------------------------------------------------------
def eliminar_coraerolinea (_nit_aerolinea):
    con = conexion_db()
    sql = f"DELETE FROM cor_aerolinea WHERE nit_aerolinea= '{_nit_aerolinea}'"

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Correo de aerolinea eliminado")
        return True

    except Error as e:
        print ("Error al eliminar el correo de la aerolinea "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

#------------------------------------------------------------------------------
def eliminar_telaerolinea (_nit_aerolinea):
    con = conexion_db()
    sql = f"DELETE FROM tel_aerolinea WHERE nit_aerolinea= '{_nit_aerolinea}'"

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Telefono de aerolinea eliminado")
        return True

    except Error as e:
        print ("Error al eliminar el correo de la aerolinea "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# //////////////////////////////////// CREAR VUELOS /////////////////////////////////////////////////
def crear_vuelo(data):
    
    con = conexion_db()

    sql = """INSERT INTO vuelo 
            (id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, fecha_vuelo, hora_vuelo, aerolinea, id_avion, id_piloto, id_copiloto, id_agenda, estado) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, data)
        con.commit()
        print("Nueva vuelo creado")
        return True

    except Error as e:
        print ("Error al crear vuelo "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# -------------------------------------------------------------------------------------------------------------
def consultar_aerolinea (_nom_aerolinea):
    
    con = conexion_db()

    sql = f""" SELECT nit_aerolinea
                FROM aerolinea 
                WHERE nom_aerolinea = '{_nom_aerolinea}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, _nom_aerolinea)
        con.commit()
        nit = cursor.fetchone()
        return nit

    except Error as e:
        print ("Error al seleccionar aerolineas: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------
def consultar_avion ():
    con = conexion_db()

    sql = """ select id_avion, tipo_avion, descripcion, tipo_propulsion, capacidad, 
            peso_nominal, num_motores from
            (avion join modelo on avion.cod_modelo = modelo.cod_modelo)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        aviones = cursor.fetchall()
        return aviones

    except Error as e:
        print ("Error al seleccionar aviones: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -----------------------------------------------------------------------------------
def seleccionar_avion (_id_avion):
    con = conexion_db()

    sql = f""" Select id_avion, tipo_avion, descripcion, tipo_propulsion, capacidad, 
                peso_nominal, num_motores from 
                (avion join modelo on avion.cod_modelo = modelo.cod_modelo)
                where id_avion = {_id_avion}"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        avion = cursor.fetchone()
        return avion

    except Error as e:
        print ("Error al seleccionar avion: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

#-------------------------------------------------------------------------------------------------------
def crear_avion (data):
    con = conexion_db()

    sql = """INSERT INTO avion 
            (id_avion, tipo_avion, cod_modelo, capacidad) 
            VALUES (%s,%s,%s,%s)"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, data)
        con.commit()
        print("Nueva avion creado")
        return True

    except Error as e:
        print ("Error al crear avion "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ----------------------------------------------------------------------------------------------
def seleccionar_todos_pilotos ():
    con = conexion_db()

    sql = """SELECT id_piloto, nom_piloto, ape_piloto, id_licencia, fecha_revmed, horas_vuelo FROM piloto"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        pilotos = cursor.fetchall()
        print(pilotos)
        return pilotos

    except Error as e:
        print ("Error al traer pilotos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------------------------------------------------------------------------
def seleccionar_todos_vuelos ():
    con = conexion_db()

    sql = """SELECT fecha_vuelo, hora_vuelo, id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado FROM vuelo
            where estado = 'Aceptado';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        vuelos = cursor.fetchall()
        print(vuelos)
        return vuelos

    except Error as e:
        print ("Error al traer todos los vuelos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# --------------------------------------------------------------------------------------------------------------------------------------------------
def seleccionar_vuelos_salida ():
    con = conexion_db()

    sql = """SELECT fecha_vuelo, hora_vuelo, id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado FROM vuelo
            where estado = 'Aceptado' and tipo_vuelo = 'Salida';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        vuelos = cursor.fetchall()
        print(vuelos)
        return vuelos

    except Error as e:
        print ("Error al traer todos los vuelos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# --------------------------------------------------------------------------------------------------------------------------------------------------
def seleccionar_vuelos_llegada ():
    con = conexion_db()

    sql = """SELECT fecha_vuelo, hora_vuelo, id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado FROM vuelo
            where estado = 'Aceptado' and tipo_vuelo = 'Llegada';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        vuelos = cursor.fetchall()
        print(vuelos)
        return vuelos

    except Error as e:
        print ("Error al traer todos los vuelos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# -------------------------------------------------------------------------------------------------
def cod_tripulacion_pasajeros():
    con = conexion_db()

    sql = """select cod_tripulacion from piloto group by 1 having count(cod_tripulacion) =2 order by 1;"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        tripulaciones = cursor.fetchall()
        print(tripulaciones)
        return tripulaciones

    except Error as e:
        print ("Error al traer las tripulaciones"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------------------------
def cod_tripulacion_carga():
    con = conexion_db()

    sql = """select cod_tripulacion from piloto group by 1 having count(cod_tripulacion) =1 order by 1;"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        tripulaciones = cursor.fetchall()
        print(tripulaciones)
        return tripulaciones

    except Error as e:
        print ("Error al traer las tripulaciones"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ----------------------------------------------------------------------------
def traer_tripulacion(_id_trip):
    con = conexion_db()

    sql = f"""select id_piloto, nom_piloto, ape_piloto, id_licencia, fecha_revmed, horas_vuelo
            from piloto where cod_tripulacion = '{_id_trip}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        tripu = cursor.fetchall()
        print(tripu)
        return tripu

    except Error as e:
        print ("Error al traer todos las tripulaciones"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------------
def consulta_tipo_vuelo (_id_avion):
    con = conexion_db()

    sql = f""" Select tipo_avion from avion where id_avion like '%{_id_avion}%'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        tipo = cursor.fetchone()
        return tipo

    except Error as e:
        print ("Error al traer el tipo de avion: "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# --------------------------------------------------------------------------------------------
def cod_piloto_copiloto (_id_trip):
    con = conexion_db()

    sql = f"""select id_piloto from piloto where cod_tripulacion ='{_id_trip}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        tripu = cursor.fetchall()
        print(tripu)
        return tripu

    except Error as e:
        print ("Error al traer todos las tripulaciones"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------------------------------------------
def vuelos_entidad (ent):
    con = conexion_db()

    sql = f"""SELECT fecha_vuelo, hora_vuelo,id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado
            FROM (vuelo join aerolinea on aerolinea = nit_aerolinea) where aerolinea = '{ent}' """

    try:
        cursor = con.cursor()
        cursor.execute (sql, ent)
        con.commit()
        vuellos = cursor.fetchall()
        print(vuellos)
        return vuellos

    except Error as e:
        print ("Error al traer todos los vuelos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# -------------------------------------------------------------------------------------------------
def vuelos_pendientes (_nit):
    con = conexion_db()

    sql = f"""SELECT fecha_vuelo, hora_vuelo,id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado
            FROM (vuelo join aerolinea on aerolinea = nit_aerolinea) where estado = 'No Enviado' 
            and aerolinea = '{_nit}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql,_nit)
        con.commit()
        vuellos = cursor.fetchall()
        print(vuellos)
        return vuellos

    except Error as e:
        print ("Error al traer todos los vuelos"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# ---------------------------------------------------------------------------------------------
def cambio_estado_espera(_nit):
    con = conexion_db()

    sql = f"""update vuelo set estado = 'En espera' where aerolinea = '{_nit}' """

    try:
        cursor = con.cursor()
        cursor.execute (sql, _nit)
        con.commit()
        print("Estado cambiado a EN ESPERA")
        return True

    except Error as e:
        print ("Error al cambiar estado "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()
# //////////////////////////////// AGENDAR EN AEROPUERTO //////////////////////////////////////////
def traer_vuelos_espera(_nit):
    con = conexion_db()

    sql = f"""SELECT hora_vuelo, fecha_vuelo, id_vuelo, tipo_vuelo, estado
            FROM (vuelo join aerolinea on aerolinea = nit_aerolinea) where estado = 'En espera' 
            and aerolinea = '{_nit}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql,_nit)
        con.commit()
        espera = cursor.fetchall()
        print(espera)
        return espera

    except Error as e:
        print ("Error al traer todos los vuelos en espera"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------
def aceptar_vuelo(_id_vuelo):
    con = conexion_db()

    sql = f"""update vuelo set estado = 'Aceptado' where id_vuelo = '{_id_vuelo}';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, _id_vuelo)
        con.commit()
        print("Estado cambiado a ACEPTADO")
        return True
        
    except Error as e:
        print ("Error al cambiar de estado"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()

# ---------------------------------------------------------------------------------
def rechazar_vuelo(_id_vuelo):
    con = conexion_db()

    sql = f"""update vuelo set estado = 'Denegado' where id_vuelo = '{_id_vuelo}';"""

    try:
        cursor = con.cursor()
        cursor.execute (sql, _id_vuelo)
        con.commit()
        print("Estado cambiado a DENEGADO")
        return True
        
    except Error as e:
        print ("Error al cambiar de estado"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()


# //////////////////////////////// ELIMINAR VUELO /////////////////////////////////////////////////
def borrar_vuelo (_id_vuelo):
    con = conexion_db()
    sql = f"DELETE FROM vuelo WHERE id_vuelo= '{_id_vuelo}'" 

    try:
        cursor = con.cursor()
        cursor.execute (sql)
        con.commit()
        print("Vuelo Eliminado")
        return True

    except Error as e:
        print ("Error al eliminar vuelo "+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()


def actualizar_vuelo (_id_vuelo, datos):
    conn = conexion_db()
    sql = f""" UPDATE vuelo SET
                            id_vuelo = %s,
                            fecha_vuelo = %s,
                            hora_vuelo = %s
                            
            WHERE id_vuelo = '{_id_vuelo}'
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql, datos)
        conn.commit()
        print("Vuelo Actualizado")
        return True

    except Error as e:
        print ("Error al actualizar vuelo "+ str(e))

    finally:
        if conn:
            cursor.close()
            conn.close()

def traer_vuelo(_id_vuelo):
    con = conexion_db()

    sql = f"""SELECT fecha_vuelo, hora_vuelo, id_vuelo, tipo_vuelo, vuelo_pascar, destino, origen, estado
            FROM (vuelo join aerolinea on aerolinea = nit_aerolinea) where id_vuelo = '{_id_vuelo}'"""

    try:
        cursor = con.cursor()
        cursor.execute (sql,_id_vuelo)
        con.commit()
        vuelo = cursor.fetchone()
        print(vuelo)
        return vuelo

    except Error as e:
        print ("Error al traer el vuelo"+ str(e))

    finally:
        if con:
            cursor.close()
            con.close()