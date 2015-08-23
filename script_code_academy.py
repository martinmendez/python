# coding: latin-1
import os, sys
# El código anterior evita problemas con el encoding del código fuente evitando que los acentos en los comentarios
# generen errores de syntaxis al ejecutar
#
#
# El codigo del pie es para explicar que el identado en python es a traves de espacios
# Si la variable huevos y return no estan identadas con un golpe de TAB este codigo da error
# Los errores de identación python los anuncia como IndentationError: expected an indented block

# """ Comentario de varias lineas entre 3 comillas: ¡Soy un leñador y me siento con energía, duermo toda la noche, y trabajo todo el día!"""

def jamon():
    huevos = 12
    return huevos

print jamon()

#¡Haz que big_var sea igual a 1 más 2 en la línea 3!
big_var = 1
big_var = big_var + 2
print big_var

# Comentario
monty = True
python = 1.234
monty_python = python ** 2
print monty_python

#¡Reasigna la comida en la línea 7!

#¡Asigna la variable total en la línea 8!

comida = 44.50
impuesto = 0.0675
propina = 0.15

comida = comida + comida * impuesto
total = comida + comida * propina

print("%.2f" % total)

# El caracter Escape para salvar caracteres especiales
# El string de la parte inferior tiene un error. ¡Corrígelo usando la barra invertida de escape!

Graham = "Help! Help! I\'m being repressed!"

"""
El string "PYTHON" tiene seis caracteres,
numerados del 0 al 5, como se muestra a continuación:

---+---+---+---+---+---+-
 P | Y | T | H | O | N |
---+---+---+---+---+---+-
 0   1   2   3   4   5

Así que si quieres recuperar "Y", podrías escribir
"PYTHON"[1] (¡comienza siempre a contar desde 0!)
o "MONTY"[4]
"""
quinta_letra = "python"[1]
quinta_letra = "MONTY"[4]
print(quinta_letra)

"""
Ahora hablaremos acerca de algunos de los métodos que están disponibles para ser usados con strings.

Un método es una función de un objeto específico (veremos los objetos más adelante). Una función es un fragmento de código
que resuelve un problema particular o que desempeña una tarea específica. (En la Unidad 4 veremos las funciones.) Por ahora,
la idea principal es que los métodos de string son fragmentos de código pre-construidos que desempeñan tareas específicas para
los strings.

En esta sección, vamos a concentrarnos en cuatro métodos de string:

len()
lower()
upper()
str()
"""

"""Asigna la variable loro en la línea 4,
luego llama a len() en loro en la línea 5!"""

loro = "Azul Noruego"
print len(loro)


#¡Usa lower() con loro, tal como se describe en las instrucciones!

loro = "Azul Noruego"

print loro.lower()
print loro.upper()

"""Declara y asigna tu variable en la línea 4,
luego, ¡llama a tu método en la línea 5!
str convierte cualquier cosa a string
"""

pi = 3.14159
print str(pi)
print str(3.14159)

"""
Notación de puntos
Como lo prometimos, ahora explicaremos la razón por la que usas len(string) y str(objeto), pero usas la notación de puntos (P.ej.,
"String".upper()) con el resto.

La notación de puntos funciona en los string literales ("The Ministry of Silly Walks".upper()) y en las variables asignadas a
los strings (ministry.upper()) porque estos métodos son específicos de los strings; es decir, no funcionan con ningún otro elemento.
En comparación, len() y str() pueden funcionar con un montón de objetos diferentes (que veremos más adelante), así que no se les puede
asociar únicamente a los strings con notación de puntos.
"""

#¡Llama a len() en la línea 4 y a upper() en la línea 5!

ministry = "The Ministry of Silly Walks"
print len(ministry)
print ministry.upper()


"""¡Dile al intérprete que muestre "Monty Python"
en la línea 4 en la consola!"""

print "Monty Python"

"Concatenacion de strings"
#¡Haz que se muestre la concatenación de "Spam 'n eggs" en la línea 3!

print "Spam " + "'n " + "eggs"

"Formateo de string con %"

camelot = "Camelot"
lugar = "lugar"
print "No vayamos a %s. Es un %s tonto." % (camelot, lugar)
