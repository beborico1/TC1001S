from turtle import *
 from freegames import floor, vector

 comparador = True
 path = Turtle(visible=False)

 mapa = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
 ]


 def square(x, y):
     "Draw square using path at (x, y)."
     path.up()
     path.goto(x, y)
     path.down()
     path.begin_fill()

 while comparador == True:
     comparador2 = True
     print(mapa)
     for x in range(20):
         for y in range(20):
             if mapa[x][y] == 0:
                 print("#", end="")
             elif mapa[x][y] == 1:
                 print("X", end="")
             elif mapa[x][y] == 2:
                 print("v", end="")
         print("")

     tecla = input()

     break_out_flag = False
     for i in range(20):
         for j in range(20):
             if mapa[i][j] == 2:
                 if tecla == "w":
                         if (mapa[i-1][j] == 1):
                             mapa[i-1][j] = 2
                             mapa[i][j] = 1
                         elif (mapa[i-1][j] == 3):
                             mapa[i-1][j] = 2
                             mapa[i][j] = 1
                             comparador = False
                         else:
                             continue
                 elif tecla == "a":
                         if (mapa[i][j-1] == 1):
                             mapa[i][j-1] = 2
                             mapa[i][j] = 1
                         elif (mapa[i][j-1] == 3):
                             mapa[i][j-1] = 2
                             mapa[i][j] = 1
                             comparador = False
                         else:
                             continue
                 elif tecla == "s":
                     if (mapa[i+1][j] == 1):
                         mapa[i+1][j] = 2
                         mapa[i][j] = 1
                         print("bajé")
                         break_out_flag = True
                         break
                     elif (mapa[i][j-1] == 3):
                         mapa[i+1][j-1] = 2
                         mapa[i+1][j] = 1
                         comparador = False
                     else:
                         continue
                 elif tecla == "d":
                     if (mapa[i][j+1] == 1):
                         mapa[i][j+1] = 2
                         mapa[i][j] = 1
                         break
                     elif (mapa[i][j+1] == 3):
                         mapa[i][j+1] = 2
                         mapa[i][j] = 1
                         comparador = False
                     else:
                         continue
                 else:
                     print("Tecla inválida")
             else:
                 continue
         if break_out_flag:
             break 
     for count in range(4):
         path.forward(24)
         path.left(90)

     path.end_fill()

 def world():
     "Draw world using path."
     bgcolor('green')

     for index in range(len(mapa)):
         tile = mapa[index]

         if tile == 1:
             path.color('grey')
             x = (index % 25) * 25 - 310
             y = 290 - (index // 25) * 25
             square(x, y)
         elif tile == 2:
             path.color('red')
             x = (index % 25) * 25 - 310
             y = 290 - (index // 25) * 25
             square(x, y)
         elif tile == 3:
             path.color('yellow')
             x = (index % 25) * 25 - 310
             y = 290 - (index // 25) * 25
             square(x, y)


 def encontrar(lista):
     for v in range(625):
         if lista[v] == 2:
             return v
         else: 
             continue


 def arriba():
     posicion = encontrar(mapa)
     if (mapa[posicion-25] == 1):
         mapa[posicion-25] = 2
         mapa[posicion] = 1
     elif (mapa[posicion-25] == 3):
         mapa[posicion-25] = 2
         mapa[posicion] = 1
         tracer(False)
         world() 
         done()


 def izquierda():
     posicion = encontrar(mapa)
     if (mapa[posicion-1] == 1):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
     elif (mapa[posicion-1] == 3):
         mapa[posicion-1] = 2
         mapa[posicion] = 1
         tracer(False)
         world() 
         done()



 def abajo():
     posicion = encontrar(mapa)
     if (mapa[posicion+25] == 1):
         mapa[posicion+25] = 2
         mapa[posicion] = 1
     elif (mapa[posicion+25] == 3):
         mapa[posicion+25] = 2
         mapa[posicion] = 1
         tracer(False)
         world() 
         done()


 def derecha():
     posicion = encontrar(mapa)
     if (mapa[posicion+1] == 1):
         mapa[posicion+1] = 2
         mapa[posicion] = 1
     elif (mapa[posicion+1] == 3):
         mapa[posicion+1] = 2
         mapa[posicion] = 1
         tracer(False)
         world() 
         done()