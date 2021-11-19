from tkinter import *
import operaciones

# Funciones para los botones
def command_read():
    lista.delete(0, END)
    lista_libros = operaciones.read()
    for libro in lista_libros:
        # con esto la insertamos tal y como se han creado en la db
        lista.insert(END, libro)

def command_search():
    lista.delete(0, END)
    lista_libros = operaciones.search(titulo.get(), autor.get(), year.get(), codigo.get())
    for libro in lista_libros:
        # con esto la insertamos tal y como se han creado en la db
        lista.insert(END, libro)

def command_insert():
    operaciones.insert(titulo.get(), autor.get(), year.get(), codigo.get())
    lista.delete(0, END)
    lista.insert(END, (titulo.get(), autor.get(), year.get(), codigo.get()))


def recoger_fila_seleccionada(event):
    try:
        global libro_seleccionado
        indice = lista.curselection()[0]
        libro_seleccionado = lista.get(indice)
        entrada1.delete(0,END)
        entrada1.insert(END, libro_seleccionado[1])

        entrada2.delete(0,END)
        entrada2.insert(END, libro_seleccionado[2])

        entrada3.delete(0,END)
        entrada3.insert(END, libro_seleccionado[3])

        entrada4.delete(0,END)
        entrada4.insert(END, libro_seleccionado[4])
    except IndexError:
        pass

def command_update():
    operaciones.update(titulo.get(), autor.get(), year.get(), codigo.get(), libro_seleccionado[0])
    lista.delete(0,END)
    lista.insert(END, 'Libro actualizado correctamente')

def command_delete():
    operaciones.delete(libro_seleccionado[0])
    lista.delete(0,END)
    lista.insert(END, 'Libro borrado correctamente')

def command_close():
    ventana.destroy()


# creación de la ventada de la aplicación
ventana = Tk()

# creación de etiquetas Label
entrada1 = Label(ventana, text='Titulo')
entrada1.grid(row=0, column=0)

entrada2 = Label(ventana, text='Autor')
entrada2.grid(row=0, column=2)

entrada3 = Label(ventana, text='Año')
entrada3.grid(row=1, column=0)

entrada4 = Label(ventana, text='Codigo')
entrada4.grid(row=1, column=2)

# entrada de datos
titulo = StringVar()
entrada1 = Entry(ventana, textvariable=titulo)
entrada1.grid(row=0, column=1)

autor = StringVar()
entrada2 = Entry(ventana, textvariable=autor)
entrada2.grid(row=0, column=3)

year = StringVar()
entrada3 = Entry(ventana, textvariable=year)
entrada3.grid(row=1, column=1)

codigo = StringVar()
entrada4 = Entry(ventana, textvariable=codigo)
entrada4.grid(row=1, column=3)

#Lista y escroll  donde se mostraran los elementos
lista = Listbox(ventana, height=8, width=25)
lista.grid(row=2, column=0, rowspan=6, columnspan=2)

# Creación de scrollback
scrollbar = Scrollbar(ventana)
scrollbar.grid(row=2, column=2, rowspan=6)

# Conexión de la lista con el escrolbar
lista.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista.yview)

# incluir un evento a la lista
lista.bind('<<ListboxSelect>>', recoger_fila_seleccionada)

# Ahora los botones en la columna 3
btn1 = Button(ventana, text="Visualizar", width=12, command=command_read)
btn1.grid(row=2, column=3)

btn2 = Button(ventana, text="Buscar", width=12, command=command_search)
btn2.grid(row=3, column=3)

btn3 = Button(ventana, text="Añadir", width=12, command=command_insert)
btn3.grid(row=4, column=3)

btn4 = Button(ventana, text="Actualizar", width=12, command=command_update)
btn4.grid(row=5, column=3)

btn5 = Button(ventana, text="Borrar", width=12, command=command_delete)
btn5.grid(row=6, column=3)

btn6 = Button(ventana, text="Cerrar", width=12, command=command_close)
btn6.grid(row=7, column=3)

# Funcionalidad para los botones
# 1- Creación de base de datos en un archivo aparte llamado operaciones
# 2- se importa el archivo operaciones al inicio de portada


# titulo y bucle principal
ventana.title("Registro de Libros")
ventana.mainloop()










