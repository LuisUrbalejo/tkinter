import tkinter as tk
import random

# 2020/05/08
# Luis Urbalejo
# Python en español (principiantes)

# Supervivencia: cada célula (digámosle ficha), que tenga dos o tres fichas vecinas sobrevive 
#                y pasa a la generación siguiente.

# Fallecimiento: cada ficha que tenga cuatro o más vecinas muere y es retirada del tablero,
#                por sobrepoblación. Las fichas con una vecina o solas fallecen por aislamiento.
# Nacimientos: cada casilla vacía, adyacente a exactamente tres cifras vecinas -tres, ni más ni menos- 
#               es casilla generatriz. Es decir, en la siguiente generación habrá de colocarse 
#               una ficha en esa casilla.


lstCeldas = []
intJuego = 0
def vecinas(y,x):      # Busca entre las 8 celdas vecinas si hay  celdas vivas
    intTotalVivas = 0
    if y - 1 >= 0:   # NORTE
        intTotalVivas += 1 if lstCeldas[y - 1][x]["bg"] == "red" else 0
    if y + 1 < len(lstCeldas):   # SUR
        intTotalVivas += 1 if lstCeldas[y + 1][x]["bg"] == "red" else 0
    if x - 1 >= 0:   # OESTE
        intTotalVivas += 1 if lstCeldas[y][x - 1]["bg"] == "red" else 0
    if x + 1 < len(lstCeldas[y]):   # ESTE
        intTotalVivas += 1 if lstCeldas[y][x + 1]["bg"] == "red" else 0
    if y - 1 >= 0 and x - 1 >=0:   #NOROESTE
        intTotalVivas += 1 if lstCeldas[y - 1][x - 1]["bg"] == "red" else 0
    if y - 1 >= 0 and x + 1 < len(lstCeldas[y]):    # NORESTE
        intTotalVivas += 1 if lstCeldas[y - 1][x + 1]["bg"] == "red" else 0
    if y + 1 < len(lstCeldas) and x - 1 >= 0:    # SUROESTE
        intTotalVivas += 1 if lstCeldas[y + 1][x - 1]["bg"] == "red" else 0
    if y + 1 < len(lstCeldas) and x + 1 < len(lstCeldas[y]):   # SURESTE
        intTotalVivas += 1 if lstCeldas[y + 1][x + 1]["bg"] == "red" else 0
    return intTotalVivas

def iniciar():   # Botón INICIAR-EDITAR
    global intJuego, btninicio
    intJuego = 1 - intJuego    # Bandera para saber si jugamos o editamos
    btninicio['text'] = "EDITAR" if intJuego == 1 else "INICIO"

def aleatoria(): # Crea celdas vacías o vivas aleatoriamente
    for y in range(len(lstCeldas)):
        for x in range(len(lstCeldas[y])):
            cel = random.randint(0,1)
            cel = "white" if cel == 0 else "red"
            lstCeldas[y][x]["bg"] = cel 

def generacion(event):  # Función cuando se da clic en una celda, crea la próxima generación
    if intJuego == 1:   # Se acuerdan de la bandera? ... Modo Jugar (INICIAR)
        lstProxGeneracion = []  # Esta será la matriz para la proxima generación, puesto que no debemos modificar hasta leer todas las celdas
        for y in range(len(lstCeldas)):
            lstLinea = []
            for x in range(len(lstCeldas[y])):
                celda = lstCeldas[y][x]["bg"]   # Color de celda actual
                intVecinas = vecinas(y,x)   # Cuantas celdas vivas alrededor?
                if celda == "white" :  # celda vacía
                    if intVecinas == 3 :   #  Nacimiento
                        celda = "red"
                elif celda == "red" :   # celda viva
                    if intVecinas == 2  or intVecinas == 3:   # Sobrevive
                        pass
                    else:  # Muere maldita celda opresora!!!!
                        celda = "white"
                # print(y,x,celda, intVecinas)
                lstLinea.append(celda)
            lstProxGeneracion.append(lstLinea)
        
        intVivas, intVacias = 0, 0  # Inicializamos un contador para celdas vivas y vacías
        for y in range(len(lstCeldas)):
            for x in range(len(lstCeldas[y])):
                lstCeldas[y][x]["bg"] = lstProxGeneracion[y][x]   # actualizamos cada celda
                intVivas += 1 if lstProxGeneracion[y][x] == "red" else 0
                intVacias += 1 if lstProxGeneracion[y][x] == "white" else 0
        intTotalCeldas = len(lstCeldas) * len(lstCeldas[y])    # Total de celdas
        if intVivas == intTotalCeldas:   # si todas las celdas son vivas
            print("Ganan Vivas!!!")
        if intVacias == intTotalCeldas:  # si todas las celdas están vacías
            print("Pierden!!!")
    else:    # Este es el modo EDITAR
        event.widget["bg"] =  "white" if event.widget["bg"] == "red" else "red"  # cambia de viva a vacía y viceversa

master = tk.Tk()  
master.title("El Juego de la vida")

master.resizable(0,0)
master.attributes("-toolwindow", 1)

intFilas, intColumnas = 15, 15   # total de filas y columnas del juego, usar con moderación :v

for y in range(intFilas):    # Se crean las celdas...uy kemosión!
    lstLinea = []
    for x in range(intColumnas):
        btn = tk.Button(master, text="  ", bg="white")   # se crea la celda vacía
        btn.bind("<Button-1>", generacion)   # pa'cuando le hagamos clic
        btn.grid(row=y, column=x)      # acomodamos la celda en su lugar
        lstLinea.append(btn)       # Guardamos las celdas de la linea x
    lstCeldas.append(lstLinea) # luego toda esa linea en la lista de lineas..UNA MATRIZ PUES!

btninicio = tk.Button(master, text="INICIAR", command=iniciar)   # el botón para iniciar o editar
btninicio.grid(row=3, column=intColumnas+1)
btnaleatorio = tk.Button(master, text="ALEATORIA", command=aleatoria) # botón para generar aleatoriamente las celdas
btnaleatorio.grid(row=5, column=intColumnas+1)
master.mainloop()

