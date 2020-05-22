import tkinter as tk
import random

# 2020/05/22
# Luis Urbalejo
# Python en español (principiantes)

intTotalFilas, intTotalColumnas = 10, 10   # total de filas y columnas del juego, usar con moderación :v
intTotalMinas = 5
lstMinas = []
lstCeldas = []
bandera = False
def vecinas(intR, intC):      # Busca entre las 8 celdas vecinas si hay  celdas vivas
    intMinasVecinas = 0
    for y in range(intR -1, intR + 2):      # 3 filas
        for x in range(intC -1, intC + 2):  # 3 columnas
            for lstMina in lstMinas:       # vemos en las 9 posiciones
                if lstMina == [y,x] :      # si hay minas
                    intMinasVecinas += 1   # las contamos
    return intMinasVecinas 

def Gane():    # Verificar si ha ganado
        intCont = 0 # contador de casillas sin abrir
        for y in range(intTotalFilas):
            for x in range(intTotalColumnas):
                if lstCeldas[y][x]["state"] == "normal":
                    intCont += 1   # la contamos
        return intCont == intTotalMinas  # regresa True si el conteo es igual a 3 (las minas)
def minasRandom(): # Crea celdas vacías o vivas aleatoriamente
    for intMina in range(intTotalMinas):
        while True:
            intR = random.randint(0, intTotalFilas-1)
            intC = random.randint(0, intTotalColumnas-1)
            if not [intR,intC] in lstMinas:
                lstMinas.append([intR, intC])
                break

def Click(y,x):
    # primero vemos si es una mina
    global bandera
    if [y,x] in lstMinas:
        for r,c in lstMinas:
            lstCeldas[r][c]["text"]=" * "
            lstCeldas[r][c]["bg"]="red"
            lstCeldas[r][c]["state"]="disabled"
            for y in range(intTotalFilas):
                for x in range(intTotalColumnas):
                    lstCeldas[y][x]["state"]="disabled"
            master.title("PERDISTE!!")
    else:
        intVecinas = vecinas(y, x)
        lstCeldas[y][x]["text"] = str(intVecinas) + "  "[0:3]
        lstCeldas[y][x]["bg"]="white"
        lstCeldas[y][x]["state"]="disabled"
        if intVecinas == 0:
            if bandera == False:
                bandera = True
                for intR in range(y -1, y + 2):      # 3 filas
                    if 0 <= intR < intTotalFilas:
                        for intC in range(x -1, x + 2):  # 3 columnas
                            if 0 <= intC < intTotalColumnas:
                                Click(intR, intC)
                bandera = False

    if Gane():
        master.title("GANASTE!!")
        for y in range(intTotalFilas):
            for x in range(intTotalColumnas):
                lstCeldas[y][x]["state"]="disabled"
    master.update_idletasks()
    
master = tk.Tk()  
master.title("Busca Bombas!")

master.resizable(0,0)
master.attributes("-toolwindow", 1)


from functools import partial
for y in range(intTotalFilas):    # Se crean las celdas...uy kemosión!
    lstLinea = []
    for x in range(intTotalColumnas):
        btn = tk.Button(master, text="    ", bg="gray", command=partial(Click,y,x) )  # se crea la celda vacía
        # btn.bind("<Button-1>", CasillaClick)   # pa'cuando le hagamos clic
        btn.grid(row=y, column=x)      # acomodamos la celda en su lugar
        lstLinea.append(btn)       # Guardamos las celdas de la linea x
    lstCeldas.append(lstLinea) # luego toda esa linea en la lista de lineas..UNA MATRIZ PUES!
minasRandom()

master.mainloop()

