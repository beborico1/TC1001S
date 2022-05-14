from turtle import *
from freegames import floor, vector

 comparador = True
 llave = False
 path = Turtle(visible=False)

 mapa = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
    0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
     0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0,
     0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0,
     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 3, 1, 1, 1, 0, 1, 1, 1, 0,
     0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
 ]

 @@ -64,6 +65,11 @@ def world():
             y = 290 - (index // 25) * 25
             square(x, y)
         elif tile == 3:
             path.color('brown')
             x = (index % 25) * 25 - 310
             y = 290 - (index // 25) * 25
             square(x, y)
         elif tile == 4:
             path.color('yellow')
             x = (index % 25) * 25 - 310
             y = 290 - (index // 25) * 25
 @@ -80,10 +86,15 @@ def encontrar(lista):

 def arriba():
     posicion = encontrar(mapa)
     global llave
     if (mapa[posicion-25] == 1):
         mapa[posicion-25] = 2
         mapa[posicion] = 1
     elif (mapa[posicion-25] == 3):
     elif (mapa[posicion-25] == 4):
         mapa[posicion-25] = 2
         mapa[posicion] = 1
         llave = True
     elif (mapa[posicion-25] == 3 and llave == True):
         mapa[posicion-25] = 2
         mapa[posicion] = 1
         tracer(False)
 @@ -93,10 +104,15 @@ def arriba():

 def izquierda():
     posicion = encontrar(mapa)
     global llave
     if (mapa[posicion-1] == 1):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
     elif (mapa[posicion-1] == 3):
     elif (mapa[posicion-1] == 4):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
         llave = True
     elif (mapa[posicion-1] == 3 and llave == True):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
         tracer(False)
 @@ -107,10 +123,15 @@ def izquierda():

 def abajo():
     posicion = encontrar(mapa)
     global llave
     if (mapa[posicion+25] == 1):
         mapa[posicion+25] = 2
         mapa[posicion] = 1
     elif (mapa[posicion+25] == 3):
     elif (mapa[posicion+25] == 4):
         mapa[posicion+25] = 2
         mapa[posicion] = 1
         llave = True
     elif (mapa[posicion+25] == 3 and llave == True):
         mapa[posicion+25] = 2
         mapa[posicion] = 1
         tracer(False)
 @@ -120,10 +141,15 @@ def abajo():

 def derecha():
     posicion = encontrar(mapa)
     global llave
     if (mapa[posicion+1] == 1):
         mapa[posicion+1] = 2
         mapa[posicion] = 1
     elif (mapa[posicion+1] == 3):
     elif (mapa[posicion-1] == 4):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
         llave = True
     elif (mapa[posicion+1] == 3 and llave == True):
         mapa[posicion+1] = 2
         mapa[posicion] = 1
         tracer(False)