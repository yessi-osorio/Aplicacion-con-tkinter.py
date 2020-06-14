from tkinter import ttk
from tkinter import *

window = Tk()

window.title("Bienvenido a la aplicacion python")
window.geometry('350x200')


etiqueta1 = Label(window, text="Nombre", font=("Arial Bold", 18)).grid(column=1, row=0)
etiqueta2 = Label(window, text="Apellido", font=("Arial Bold", 18)).grid(column=1, row=1)
etiqueta3 = Label(window, text="Dia", font=("Arial Bold", 18)).grid(column=1, row=2)
etiqueta4 = Label(window, text="Mes", font=("Arial Bold", 18)).grid(column=1, row=3)
etiqueta5 = Label(window, text="Año", font=("Arial Bold", 18)).grid(column=1, row=4)

btn = Button(window, text="Funcion1", bg="orange", fg="red", font=("Arial Bold", 15)).grid(column=3, row=0)
btn = Button(window, text="Funcion2", bg="orange", fg="red", font=("Arial Bold", 15)).grid(column=3, row=1)
btn = Button(window, text="Funcion3", bg="orange", fg="red", font=("Arial Bold", 15)).grid(column=3, row=2)
btn = Button(window, text="Funcion4", bg="orange", fg="red", font=("Arial Bold", 15)).grid(column=3, row=3)
btn = Button(window, text="Funcion5", bg="orange", fg="red", font=("Arial Bold", 15)).grid(column=3, row=4)

txt = Entry(window,width=25).grid(column=2, row=0)
txt = Entry(window,width=25).grid(column=2, row=1)
txt = Entry(window,width=25).grid(column=2, row=2)
txt = Entry(window,width=25).grid(column=2, row=3)
txt = Entry(window,width=25).grid(column=2, row=4)

def clicked():
    lbl.configure(text="Button was clicked !!")
    res = "Bienvenido a" + txt.get()
    lbl.configure(text= res)

btn = Button(window, text="Funcion1", command=clicked).grid(column=3, row=0)
btn = Button(window, text="Funcion2", command=clicked).grid(column=3, row=1)
btn = Button(window, text="Funcion3", command=clicked).grid(column=3, row=2)
btn = Button(window, text="Funcion4", command=clicked).grid(column=3, row=3)
btn = Button(window, text="Funcion5", command=clicked).grid(column=3, row=4)



window.mainloop()