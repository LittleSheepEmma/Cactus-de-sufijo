from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from typing import IO
import numpy as np

raiz = Tk()

class FilePrinter:
    """
    Clase para imprimir caracteres en una cuadrícula y obtener su representación en texto.
    """
    def __init__(self):
        """
        Inicializa la cuadrícula y las dimensiones.
        """
        self.width = 0
        self.heigth = 0
        self.grid = np.full(fill_value=" ", shape=(255, 255))
        pass

    def print_character(self, value, x, y):
        """
        Imprime un carácter en la posición (x, y) de la cuadrícula.
        """
        self.grid[y][x] = value
        pass

    def get_text(self):
        """
        Devuelve la representación en texto de la cuadrícula (primeros 50x50).
        """
        txt = ""
        for i in range(50):
            for j in range(50):
                txt = txt + self.grid[i][j]
            txt = txt + "\n"
        
        return txt
    
    def print_to_console(self):
        """
        Imprime la cuadrícula en la consola.
        """
        print(self.get_text())


raiz.title("Cactus de Sufijo")
#raiz.iconbitmap("iconoCactus.ico")
raiz.geometry("600x980")


contenido_archivo = ""

miFrame = Frame(raiz, width = 590, height = 800)
Frame1 = Frame(raiz, width = 590, height = 25)
Frame2 = Frame(raiz, width = 590, height = 25)

Frame1.pack()
Frame2.pack()
miFrame.pack()

Label(Frame1, text = "Cactus de Sufijo", font = ("Bahnschrift SemiBold",18)).grid(row = 0, columnspan = 10)
Label(Frame1, text = "Puedes Ingresar el string desde el cuadro de texto o desde un archivo TXT", font = ("Bahnschrift SemiBold",8)).grid(row = 1, columnspan = 10)
Label(Frame1, text = "Por favor, ingresa el texto sin espacios y con terminacion $", font = ("Bahnschrift SemiBold",8)).grid(row = 2, columnspan = 10)


ListaSufijos = []
ListaProf = []
#Funcion de profundidad
def depth(s1, s2):
    """
    Calcula la profundidad (longitud del prefijo común) entre dos cadenas.
    """
    String1 = s1
    String2 = s2
    profundidad = 0
    for i in range(len(s1)):
        if(String1[i] == String2[i]):
            profundidad += 1
        else:
            break
    return profundidad
#Funcion de Alternativa 1
def CactusSuf(Cadena):
    """
    Construye e imprime el cactus de sufijos usando la alternativa 1.
    """
    global contenido_archivo
    ListaProf.clear()
    ListaSufijos.clear()
    ArregloRaiz = []
    ArregloSuf = []
    ArregloRama = []
    #Definir arreglo de nodos padre
    for i in range(len(Cadena)-1,-1,-1):
        if((Cadena[i] not in ArregloRaiz) and (i != len(Cadena) - 1)):
            ArregloRaiz.append(Cadena[i])
    ArregloRaiz = sorted(ArregloRaiz) 

    #Funcion de Rama Padre
    def RamaPadre(Cadena, Arreglo, Limite):
        """
        Calcula la profundidad de la rama padre para un sufijo dado.
        """
        Limitador = Arreglo.index(Arreglo[Limite])
        profundidad = depth(Cadena,Arreglo[Limite])
        for i in range(len(Arreglo[:Limitador]),-1,-1):
            Sufijo = Arreglo[Limite]
            if(depth(Arreglo[i],Arreglo[Limite]) > profundidad and Arreglo[i] != Sufijo):
                profundidad = depth(Arreglo[i], Sufijo)
                break
        return profundidad
      
    #Definir arreglo de ramas padre
    for i in range(len(ArregloRaiz)):
        Caracter = ArregloRaiz[i]
        for n in range(len(Cadena)-1,-1,-1):
            if(Cadena[n] == Caracter):
                ArregloRama.append(Cadena[n:])
                break
    ArregloRama = sorted(ArregloRama)
        
    #Definir arreglo de sufijos
    for i in range(len(ArregloRaiz)):
        Caracter = ArregloRaiz[i]
        for n in range(len(Cadena)-1,-1,-1):
            if(Cadena[n] == Caracter and (Cadena[n:] not in ArregloRama)):
                ArregloSuf.append(Cadena[n:])
                
    ArregloSuf = sorted(ArregloSuf)
    
    #Imprimir Cactus de Sufijo

    file_printer = FilePrinter()
    LCP = 0
    PosX = 5
    PosY = 8
    for i in range(len(ArregloRama)):
        PosY = 8
        PosX = PosX + 1
        Label(miFrame, text = " ", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
        PosX = PosX + 1
        for y in range(len(ArregloRama[i])):
            Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
            file_printer.print_character("|", PosX, PosY)
            PosY = PosY + 1
        PosX = PosX + 1
        PosY = 8
        for k in range(len(ArregloRama[i])):
            Label(miFrame, text = ArregloRama[i][k], font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
            file_printer.print_character(ArregloRama[i][k], PosX, PosY)
            PosY = PosY + 1
        PosX = PosX + 1
        PosY = 8
        for y in range(len(ArregloRama[i])):
            Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
            file_printer.print_character("|", PosX, PosY)
            PosY = PosY + 1
        PosX = PosX + 1
        PosY = 8
        ListaSufijos.append(ArregloRama[i])
        ListaProf.append(0)
        for n in range(len(ArregloSuf)):
            PosY = 8
            if(ArregloSuf[n][0] == ArregloRama[i][0]):
                LCP = RamaPadre(ArregloRama[i], ArregloSuf, n)
                PosY = PosY + LCP
                ListaSufijos.append(ArregloSuf[n][LCP:])
                ListaProf.append(LCP)
                Label(miFrame, text = "→", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                file_printer.print_character("→", PosX, PosY)
                PosX = PosX + 1
                for y in range(len(ArregloSuf[n])):
                    if(y >= LCP):
                        Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                        file_printer.print_character("|", PosX, PosY)
                        PosY = PosY + 1
                PosY = 8
                PosY = PosY + LCP
                PosX = PosX + 1
                for j in range(len(ArregloSuf[n])):
                    if(j >= LCP):
                        Label(miFrame, text = ArregloSuf[n][j], font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                        file_printer.print_character(ArregloSuf[n][j], PosX, PosY)
                        PosY = PosY + 1
                        
                PosX = PosX + 1
                PosY = 8
                PosY = PosY + LCP
                for y in range(len(ArregloSuf[n])):
                    if(y >= LCP):
                        Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                        file_printer.print_character("|", PosX, PosY)
                        PosY = PosY + 1
                PosY = 8
                PosX = PosX + 1

    contenido_archivo = "Alternativa 1\n" + file_printer.get_text() + "\n"

def Alt2(Cadena):
    """
    Construye e imprime el cactus de sufijos usando la alternativa 2.
    """
    global contenido_archivo
    ListaSufijos.clear()
    ListaProf.clear()
    ArregloRaiz = []
    ArregloSuf = []
    ArregloRama = []
    #Definir arreglo de nodos padre
    for i in range(len(Cadena)-1,-1,-1):
        if((Cadena[i] not in ArregloRaiz) and (i != len(Cadena) - 1)):
            ArregloRaiz.append(Cadena[i])
    ArregloRaiz = sorted(ArregloRaiz) 
    #Definir arreglo de ramas padre
    for i in range(len(ArregloRaiz)):
        Caracter = ArregloRaiz[i]
        for n in range(len(Cadena)):
            if(Cadena[n] == Caracter):
                ArregloRama.append(Cadena[n:])
                break
    ArregloRama = sorted(ArregloRama)
        
    #Definir arreglo de sufijos
    for i in range(len(ArregloRaiz)):
        Caracter = ArregloRaiz[i]
        for n in range(len(Cadena)-1,-1,-1):
            if(Cadena[n] == Caracter):
                ArregloSuf.append(Cadena[n:])
                
    ArregloSuf = sorted(ArregloSuf)
    
   
    #Imprimir Cactus de Sufijo

    file_printer = FilePrinter()

    LCP = 0
    PosX = 5
    PosY = 8
    LCPAlt = 0
    for i in range(len(ArregloSuf)):
        LCPAlt = 0
        PosY = 8
        PosX = PosX + 1
        if(ArregloSuf[i] not in ArregloRama):
            for j in range(len(ArregloRama)):
                LCP = depth(ArregloRama[j],ArregloSuf[i])
                if(i < len(ArregloSuf)-1):
                    if(ArregloSuf[i+1][0] == ArregloSuf[i][0] and ArregloSuf[i+1] not in ArregloRama):
                        LCPAlt = depth(ArregloRama[j], ArregloSuf[i+1])
                    elif(ArregloSuf[i+1] in ArregloRama and ArregloSuf[i][0] == ArregloSuf[i+1][0]):
                        LCPAlt = LCP
                    else:
                        LCPAlt = 0
                else:
                    LCPAlt = 0
                if(LCP != 0):
                    break
        else:
            LCP = 0
            if(i < len(ArregloSuf)-1):
                if(ArregloSuf[i][0] == ArregloSuf[i+1][0]):
                    LCPAlt = depth(ArregloSuf[i],ArregloSuf[i+1])
                else:
                    LCPAlt = 0
            
        ListaSufijos.append(ArregloSuf[i][LCP:])
        ListaProf.append(LCP)
        PosY = PosY + LCP
        for y in range(len(ArregloSuf[i])):
            if(y >= LCP):
                Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                file_printer.print_character("|", PosX, PosY)
                PosY = PosY + 1
        PosY = 8
        PosY = PosY + LCP
        PosX = PosX + 1
        for k in range(len(ArregloSuf[i])):
            if(k >= LCP):
                Label(miFrame, text = ArregloSuf[i][k], font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                file_printer.print_character(ArregloSuf[i][k], PosX, PosY)
                PosY = PosY + 1
        PosY = 8
        PosY = PosY + LCP
        PosX = PosX + 1
        for y in range(len(ArregloSuf[i])):
            if(y >= LCP):
                Label(miFrame, text = "|", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
                file_printer.print_character("|", PosX, PosY)
                PosY = PosY + 1
        PosY = 8
        PosX = PosX + 1
        if(LCPAlt != 0):
            if(LCP < LCPAlt and ArregloSuf[i] not in ArregloRama):
                PosY = PosY + LCP    
            else:
                PosY = PosY + LCPAlt
            Label(miFrame, text = "→", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
            file_printer.print_character("→", PosX, PosY)
        else:
            Label(miFrame, text = " ", font = ("Bahnschrift SemiBold",10)).grid(row = PosY, column = PosX)
            file_printer.print_character(" ", PosX, PosY)
        PosY = 8
        PosX = PosX + 1
    
    contenido_archivo = contenido_archivo + "Alternativa 2\n" + file_printer.get_text()

#Limpiar el frame del Cactus de Sufijo anterior    
def clear_frame():
    """
    Limpia todos los widgets del frame principal.
    """
    for widgets in miFrame.winfo_children():
        widgets.destroy()
      
CadenaString = StringVar()
CuadroInput = Entry(Frame2, textvariable = CadenaString)
CuadroInput.grid(row = 1, column = 1)

NombreCuadro = Label(Frame2, text = "String: ", font = ("Bahnschrift SemiBold",14))
NombreCuadro.grid(row = 1, column = 0)

# Tooltip simple para Entry
def create_tooltip(widget, text):
    """
    Crea un tooltip simple para un widget de Tkinter.
    """
    tooltip = None
    def on_enter(event):
        nonlocal tooltip
        x = widget.winfo_rootx() + 20
        y = widget.winfo_rooty() + 20
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.geometry(f"+{x}+{y}")
        label = tk.Label(tooltip, text=text, background="#ffffe0", relief="solid", borderwidth=1, font=("Arial", 9))
        label.pack()
    def on_leave(event):
        nonlocal tooltip
        if tooltip:
            tooltip.destroy()
            tooltip = None
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

create_tooltip(CuadroInput, "Por favor, ingresa unicamente texto sin espacios y añade un $ al final del string")




def TablaDeProfundidad():
    """
    Muestra la tabla de sufijos y sus profundidades en el frame principal.
    """
    clear_frame()
    
    Label(miFrame, text = "Sufijo", font = ("Bahnschrift SemiBold",12)).grid(row = 0, column = 1)
    Label(miFrame, text = "Profundidad", font = ("Bahnschrift SemiBold",12)).grid(row = 0, column = 2)
    for i in range(len(ListaSufijos)):
        SufijoText = ListaSufijos[i]
        ProfundidadSuf = str(ListaProf[i])
        Label(miFrame, text = SufijoText, font = ("Bahnschrift SemiBold",10)).grid(row = i+1, column = 1)
        Label(miFrame, text = ProfundidadSuf, font = ("Bahnschrift SemiBold",10)).grid(row = i+1, column = 2)


CadenaString = StringVar()
CuadroInput = Entry(Frame2, textvariable = CadenaString)
CuadroInput.grid(row = 1, column = 1)

NombreCuadro = Label(Frame2, text = "String: ", font = ("Bahnschrift SemiBold",14))
NombreCuadro.grid(row = 1, column = 0)
create_tooltip(CuadroInput, "Por favor, ingresa unicamente texto sin espacios y añade un $ al final del string")


def DialogoCargarArchivo():
    """
    Abre un diálogo para cargar un archivo de texto y valida el string leído.
    """
    try:
        archivo = filedialog.askopenfilename(title="Cargar archivo de texto plano", filetypes=[("Archivo de texto plano", "*.txt")])
        if archivo:
            with open(archivo, 'r', encoding='utf-8') as f:
                string = f.readline().strip()  # Elimina saltos de línea
            if string.endswith("$") and ' ' not in string:
                CadenaString.set(string)
            elif ' ' in string:
                messagebox.showinfo(
                    message = "Por favor, ingrese el texto sin espacios", 
                    title = "ERROR: Espacios en blanco detectados")
            elif not string.endswith("$"):
                messagebox.showinfo(
                    message = "Por favor, coloque un $ al final del string para la terminacion en hoja", 
                    title = "ERROR: No hay una hoja para finalizar el string")
    except UnicodeDecodeError:
        messagebox.showinfo(
            message = "Por favor, solo ingrese archivos de texto plano", 
            title = "ERROR: Solo se aceptan archivos de texto plano")
    except Exception:
        messagebox.showinfo(
            message = "Ocurrió un error al leer el archivo", 
            title = "ERROR: No se pudo leer el archivo, es probable que esté corrupto o no sea texto plano.")

def CargarString():
    """
    Valida el string ingresado y construye el cactus de sufijos (alternativa 1).
    """
    clear_frame()
    CadenaCactus = CuadroInput.get()
    EspacioBlanc = False
    Hoja = False
    for i in range(len(CadenaCactus)):
        if(CadenaCactus[i] == " "):
            EspacioBlanc = True
            break
        
    if(CadenaCactus.endswith("$")):
        Hoja = False
    else:
        Hoja = True
    if(EspacioBlanc == True):
        messagebox.showinfo(message = "Por favor, ingrese el texto sin espacios", title = "ERROR: Espacios en blanco detectados")
    elif(Hoja == True):
        messagebox.showinfo(message = "Por favor, coloque un $ al final del string para la terminacion en hoja", title = "ERROR: No hay una hoja para finalizar el string")
    else:
        CadenaCactus = CadenaCactus.upper()
        CactusSuf(CadenaCactus)
        botonTabla = Button(Frame2, text = "Tabla de Profundidad", command = TablaDeProfundidad)
        botonTabla.grid(row = 5, column = 0)

def CargarString2():
    """
    Valida el string ingresado y construye el cactus de sufijos (alternativa 2).
    """
    clear_frame()
    CadenaCactus = CuadroInput.get()
    EspacioBlanc = False
    Hoja = False
    for i in range(len(CadenaCactus)):
        if(CadenaCactus[i] == " "):
            EspacioBlanc = True
            break
    if(CadenaCactus.endswith("$")):
        Hoja = False
    else:
        Hoja = True
    if(EspacioBlanc == True):
            messagebox.showinfo(message = "Por favor, ingrese el texto sin espacios", title = "ERROR: Espacios en blanco detectados")
    elif(Hoja == True):
        messagebox.showinfo(message = "Por favor, coloque un $ al final del string para la terminacion en hoja", title = "ERROR: No hay una hoja para finalizar el string")
    else:
        CadenaCactus = CadenaCactus.upper()
        Alt2(CadenaCactus)
        botonTabla = Button(Frame2, text = "Tabla de Profundidad", command = TablaDeProfundidad)
        botonTabla.grid(row = 5, column = 0)

def ComputarYGuardar():
    """
    Ejecuta ambas alternativas y guarda el resultado en un archivo de texto.
    """
    """
    Ejecuta ambas alternativas y guarda el resultado en un archivo de texto.
    """
    clear_frame()
    CadenaCactus = CuadroInput.get()
    EspacioBlanc = False
    Hoja = False
    for i in range(len(CadenaCactus)):
        if(CadenaCactus[i] == " "):
            EspacioBlanc = True
            break
    if(CadenaCactus.endswith("$")):
        Hoja = False
    else:
        Hoja = True
    if(EspacioBlanc == True):
        messagebox.showinfo(message = "Por favor, ingrese el texto sin espacios", title = "ERROR: Espacios en blanco detectados")
        return
    elif(Hoja == True):
        messagebox.showinfo(message = "Por favor, coloque un $ al final del string para la terminacion en hoja", title = "ERROR: No hay una hoja para finalizar el string")
        return
    else:
        CadenaCactus = CadenaCactus.upper()
        global contenido_archivo
        contenido_archivo = ""
        CactusSuf(CadenaCactus)
        Alt2(CadenaCactus)
        with open("resultado.txt", "w", encoding='utf-8') as archivo:
            archivo.write(contenido_archivo)
        messagebox.showinfo(message = "Resultado guardado en resultado.txt", title = "Guardado exitoso")

botonCargar = Button(Frame2, text="Alternativa 1", command = CargarString)
botonCargar.grid(row = 3, column = 0 )
botonCargar2 = Button(Frame2, text = "Alternativa 2", command = CargarString2)
botonCargar2.grid(row = 4, column = 0)
botonCargarArchivo = Button(Frame2, text="Cargar archivo", command=DialogoCargarArchivo)
botonCargarArchivo.grid(row = 2, column=0)
create_tooltip(botonCargarArchivo, "Por favor, ingresa unicamente archivos con una sola linea de texto, sin espacios y añade un $ al final del string")
botonGuardar = Button(Frame2, text = "Computar y guardar", command=ComputarYGuardar)
botonGuardar.grid(row=6, column=0)

raiz.mainloop()
