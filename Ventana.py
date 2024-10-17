import tkinter
from tkinter import filedialog 
from tkinter import Tk, Frame, Entry, ttk

#------------ventana--------------------
ventana = tkinter.Tk()
ventana.title("Algoritmo Thompson") # nombre de la ventana 
ventana.geometry("600x600") #define tamaño de la ventana 
ventana.config(bg="white")
ventana.resizable(0,0) #para no cambiar el tamaño de la ventana 

cabezera1 =tkinter.Label(ventana, text = "Seleccione una expresion regular: ",font=("Arial", 13))#.pack()# .pack() para que se muestre dentro de la ventana 
cabezera1.pack()
cabezera1.config(bg="white")
cabezera1.place(x=12, y=4)

cabezera2 =tkinter.Label(ventana, text = "Expresion regular seleccionada: ",font=("Arial", 13)) 
cabezera2.pack()
cabezera2.config(bg="white")
cabezera2.place(x=12, y=40)

cabezera3 =tkinter.Label(ventana, text = "Alfabeto:",font=("Arial", 13))
cabezera3.pack()
cabezera3.config(bg="white")
cabezera3.place(x=12, y=75)

#Variables Globales-----------------------

EspresionRegular = ""
Alfabeto = ""

# Etiqueta que mostrará la expresión regular seleccionada

# Crear un Frame para actuar como el borde
frame_borde = tkinter.Frame(ventana, bg="lightgray", bd=1)  # Color del borde rojo, grosor 2 píxeles
frame_borde.place(x=300, y=40, width=210, height=20)  # Especificamos el tamaño del Frame

# Crear la etiqueta dentro del Frame (cuadro con texto)
cuadro_texto1 = tkinter.Label(frame_borde, text=EspresionRegular, bg="white", width=30, height=1)
cuadro_texto1.pack(fill="both", expand=True)  # La etiqueta ocupa todo el espacio del Frame


frame_borde2 = tkinter.Frame(ventana, bg="lightgray", bd=1)
frame_borde2.place(x=300, y=75, width=210, height=20)  
cuadro_texto2 = tkinter.Label(frame_borde2, text = Alfabeto, bg="white", width=30, height=1)
cuadro_texto2.pack(fill="both", expand=True)

#-------------------función----------------

def Etiqueta1(): 
    filepath = filedialog.askopenfilename(title="Escoge tu archivito :)", filetypes=(('Archivos de texto','.txt'),("Todos los archivos",".*")))
    archivo = open(filepath, 'r')
    Arrglo = []
    if archivo:
        for linea in archivo:
            Arrglo.append(linea.strip())  # .strip() para eliminar saltos de línea
             
    global EspresionRegular 
    EspresionRegular = Arrglo[1]  # Segundo elemento del archivo
    global Alfabeto
    Alfabeto = Arrglo[0]  # Primer elemento del archivo
    
    # Actualizar el texto de la etiqueta con la expresión regular seleccionada
    cuadro_texto1.config(text=EspresionRegular)
    cuadro_texto2.config(text=Alfabeto)
    
    
    archivo.close()

# Botón para abrir archivo
boton = tkinter.Button(ventana, text="Abrir", command= Etiqueta1, fg="red" )
boton.pack()  # separado para poder hacer modificaciones después al botón 
boton.place(x=300, y=2, width=100)  # ubicar botón en la ventana



table = ttk.Treeview(ventana,columns=('col1','col2','col3'))

table.column("#0",width=80)
table.column("col1",width=85)
table.column("col2",width=80)
table.column("col3",width=80)
#table.place(x=130,y=100)

table.heading("#0",text="Estados",anchor="center")
table.heading("col1",text="Transiciones 2",anchor="center")
table.heading("col2",text="Transiciones",anchor="center")
table.heading("col3",text="Epsilon",anchor="center")


table.pack(pady=120)

ventana.mainloop() # muestra la ventana








