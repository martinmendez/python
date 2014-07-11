__author__ = 'martinmendez'
from pymongo import *

print "Conectando al Servidor de Base de Datos Local..."
conexion = Connection() # Conexion local por defecto

#conexion = Connection("usuario:password@servidor.com:27075/basededato") #Conexion a un servidor remoto

#creando/obteniendo un objeto que referencie a la base de datos.
db = conexion['node-mongo-recipe'] #base de datos a usar


#retrieve a collection
col = db.recipes

#retrieve a random document - READ
doc = col.find_one()
print doc