from tkinter import *

# Funcion para imprimir los valores que se guardaron
def codigoBoton():
    nombre_data= Nombre.get()
    apellidoP_data= ApellidoP.get()
    apellidoM_data= ApellidoM.get()
    matricula_data= str(Matricula.get())
    edad_data= str(Edad.get())
    direccion_data= str(Direccion.get())
    codigo_data= str(Codigo.get())
    telefono_data =str(Telefono.get())

    print(f"Los valores recopilados son: \n{nombre_data} \n{apellidoP_data} \n{apellidoM_data} \n{matricula_data} \n{edad_data} \n{direccion_data} \n{codigo_data} \n{telefono_data}")

raiz=Tk()
raiz.title("Data Capture")
raiz.config(bg="#544471")
title= Label(text="Captura De Datos Con Python", bg= "#544471", fg="white", font=("Kristen ITC", 14))
title.grid(row=0, column=1, sticky="w")

# Creando los labels para identificar cada input
nombre_label = Label(text="Nombres", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
nombre_label.grid(row=1, column=0, padx=20, pady=15)
ApellidoP_label = Label(text="Apellido Paterno", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
ApellidoP_label.grid(row=2, column=0, padx=20, pady=15)
ApellidoM_label = Label(text="Apellido Materno", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
ApellidoM_label.grid(row=3, column=0, padx=20, pady=15)
matricula_label = Label(text="Matricula", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
matricula_label.grid(row=4, column=0, padx=20, pady=15)
edad_label = Label(text="Edad", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
edad_label.grid(row=5, column=0, padx=20, pady=15)
direccion_label = Label(text="Dirección", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
direccion_label.grid(row=6, column=0, padx=20, pady=15)
codigo_label = Label(text="Codigo Postal", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
codigo_label.grid(row=7, column=0, padx=20, pady=15)
telefono_label = Label(text="Telefono", bg="#8a8b9d", fg="white", font=("Lucida Calligraphy", 11))
telefono_label.grid(row=8, column=0, padx=20, pady=15)

# Creando variables para asignarlas a los input
Nombre = StringVar()
ApellidoP = StringVar()
ApellidoM = StringVar()
Matricula = StringVar()
Edad = StringVar()
Direccion = StringVar()
Codigo = StringVar()
Telefono = StringVar()

# Creando los input y asignandoles la variable para que puedan guardar el dato
nombre_entry= Entry(textvariable=Nombre, width="40")
apellidoP_entry= Entry(textvariable=ApellidoP, width="40")
apellidoM_entry= Entry(textvariable=ApellidoM, width="40")
matricula_entry= Entry(textvariable=Matricula, width="40")
edad_entry= Entry(textvariable=Edad, width="40")
direccion_entry= Entry(textvariable=Direccion, width="40")
codigo_entry= Entry(textvariable=Codigo, width="40")
telefono_entry= Entry(textvariable=Telefono, width="40")

# Acomodando los input en el grid
nombre_entry.grid(row=1, column=1)
nombre_entry.config(cursor="circle")
apellidoP_entry.grid(row=2, column=1)
apellidoP_entry.config(cursor="circle")
apellidoM_entry.grid(row=3, column=1)
apellidoM_entry.config(cursor="circle")
matricula_entry.grid(row=4, column=1)
matricula_entry.config(cursor="circle")
edad_entry.grid(row=5, column=1)
edad_entry.config(cursor="circle")
direccion_entry.grid(row=6, column=1)
direccion_entry.config(cursor="circle")
codigo_entry.grid(row=7, column=1)
codigo_entry.config(cursor="circle")
telefono_entry.grid(row=8, column=1)
telefono_entry.config(cursor="circle")

# Creando el boton de guardar que activa la funcion
botonEnviar=Button(raiz, text="Guardar", command=codigoBoton)
botonEnviar.config(cursor="dotbox", font=("Segoe Print", 10))
botonEnviar.grid(row=9, column=1)

# Para mostrar la pantalla
raiz.mainloop()