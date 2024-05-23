from tkinter import *

raiz=Tk()

raiz.title("I Love You So Much")


raiz.config(bg="light pink")

miFrame=Frame()

miFrame.pack(fill="y", expand="False")

miImagen=PhotoImage(file="imagen.gif")

miFrame.config(bg="purple")

miFrame.config(width="550", height="450")

miFrame.config(bd=15)

miFrame.config(relief="sunken")

miFrame.config(cursor="circle")
#dotbox
miLabel= Label(miFrame, text="Primera interfaz con tkinter", fg="gray", font=("Kristen ITC", 13))

miLabel.grid(row=0, column=0, padx=20, pady=15)
#miLabel.place(x=10, y=10)
miLabel= Label(miFrame, image=miImagen)
miLabel.grid(row=1, column=0, padx=20, pady=15)
#miLabel.place(x=25, y=100)

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=2, column=1, sticky="w")
cuadroNombre.config(fg="black", justify="center", font=("Segoe Print", 11))
#Para contraseñas: cuadroNombre.config(show="*")

nombreLabel=Label(miFrame, text="Opinión: ")
nombreLabel.grid(row=2, column=0, sticky="e")
nombreLabel.config(fg="blue", font=("Harlow Solid Italic", 18))

def codigoBoton():
    minombre.set("Usando una funcion")

botonEnviar=Button(raiz, text="Enviar", command=codigoBoton)
botonEnviar.config(cursor="dotbox", font=("Segoe Print", 10))

botonEnviar.pack()

raiz.mainloop()

