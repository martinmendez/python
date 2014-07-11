#Tutorial introductorio a Python en http://www.afterhoursprogramming.com/tutorial/Python/


# Esto es un comentario en Python

print ("print stdout")
print ("print 2 stdout")

# Otra forma de escribir print
print "print 3"

'''
Estos son comentario de mas
de una linea.
Se abren con 3 quotes y se
cierran con 3 quotes
'''
a=10
b=6
print(a+b)
#El resultado es 16
#Cuando uso comillas entre varialbes concateno los caracteres

a="20"
b="6"
print (a+b)
# El resultado es 206

#Operando con integers (variable to integers)
a="5"
b=6
print(int(a)+b)

#Operando con decimales (variable to decimales)
a="0.5"
b=6
print(float(a)+b)

#Operando con strings (variable to stings)
a="10"
print(str(a))

#Operadores en Python
print "Operadores en Python"
print (3+6)
print (100/10)
print (5*5)
print (2**3)
#otra forma de elevar al cubo
c=2
c**=3
print (c)

#esta cuenta da cero
b=2
b+=-2
print (b)

#Python if statement
print "a=20 chequea primero si a es mayor o igual a 22,"
print " no lo es. Con elif chequea si es igual o mayor a 21, no lo es,por lo que salta al else final"
# el identado de 2 espacios (o cualquier cantidad de espacio pero siempr igual) es importante !!!!
# los dos puntos al final de las variables y del else son mandatorios
a = 20
if a >= 22:
  print("if")
elif a >= 21:
  print("elif")
else:
  print("else")

#Funciones en Python. Tipicamente para codigo que vamos a reutilizar, podemos agregar parametros a la funcion

def someFunction():
  print("boo")
someFunction()

def someFunction(a, b):
  print(a+b)
someFunction(12,451)

#Arranca en 0 e incrementa hasta 8. Siempre para "right after - antes" en el rango definido
for a in range(0,9):
  print (a)

#While loops in Python
print("while loops in Python")
a = 1
while a < 10:
    print (a)
    a+=1
