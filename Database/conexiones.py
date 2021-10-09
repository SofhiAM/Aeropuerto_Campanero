import psycopg2
from psycopg2 import Error

def conexion_db():
    conexion = psycopg2.connect( host = "localhost",
                            database="aeropuerto_campanero", 
                            user="postgres", 
                            password="Jen.6505")
    return conexion
