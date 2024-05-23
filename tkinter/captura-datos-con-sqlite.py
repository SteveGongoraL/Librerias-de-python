from tkinter import *
import sqlite3

def create():
    conn=sqlite3.connect('database_tkinter.db')
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS alumno(matricula integer primary key autoincrement, nombre TEXT, apellido TEXT, edad integer, LugarNacimiento TEXT, EstadoCivil TEXT, CP integer, Telefono integer)")
    conn.commit()
    conn.close()

create()

def guardar_dato() :
    matricula_dato= matricula.get()
    matricula_dato=str(matricula_dato)
    nombre_dato= nombre.get()
    apellido_dato= apellido.get()
    edad_dato= edad.get()
    edad_dato=str(edad_dato)
    lugarnacimiento_dato = lugarnacimiento.get()
    estadocivil_dato= estadocivil.get()
    CP_dato= CP.get()
    CP_dato=str(CP_dato)
    telefono_dato= telefono.get()
    telefono_dato=str(telefono_dato)

    conn= sqlite3.connect('database_tkinter.db')
    c=conn.cursor()
    c.execute('INSERT INTO alumno(matricula,nombre,apellido,edad, LugarNacimiento,EstadoCivil,CP, telefono)VALUES(?,?,?,?,?,?,?,?)',(matricula.get(),nombre.get(),apellido.get(),edad.get(),lugarnacimiento.get(),estadocivil.get(),CP.get(),telefono.get()))
    conn.commit()

    file= open("tarea_9-7-202.txt", "w")
    file.write('Matricula: ' +matricula_dato +'\t')
    file.write('Nombre: '+nombre_dato+'\t')
    file.write('Apellido: '+apellido_dato+'\t')
    file.write('Edad: '+edad_dato+'\t')
    file.write('Lugar de Nacimiento: '+lugarnacimiento_dato+'\t')
    file.write('Estado Civil: '+estadocivil_dato+'\t')
    file.write('Codigo Postal: '+CP_dato+'\t')
    file.write('Telefono: '+telefono_dato)
    file.close
    print(" Alumno: ", matricula_dato, nombre_dato, " se ha registrado en el sistema.")

    matricula_captura.delete(0, END)
    nombre_captura.delete(0, END)
    apellido_captura.delete(0, END)
    edad_captura.delete(0, END)
    lugarnacimiento_captura.delete(0, END)
    estadocivil_captura.delete(0, END)
    CP_captura.delete(0, END)
    telefono_captura.delete(0, END)



#pantalla = Tk() #GUI
#pantalla.geometry("650x650") #Tamaño de ventana
#pantalla.title("TAREA") #nombre de la ventana
#encabezado = Label(text = "Pantalla de Captura", bg= "red", fg = "black", width = "25", height = "3")
#encabezado.pack()

#pantalla = Tk() #GUI
#pantalla.geometry("650x650") #Tamaño de ventana
#pantalla.title("TAREA") #nombre de la ventana
#pantalla.configure(bg = "#5F9EA0")
#encabezado = Label(text = "Pantalla de Captura", bg= "#5F9EA0", fg = "black", width = "25", height = "3")
#encabezado.pack()


pantalla = Tk()
pantalla.title("TAREA")
fgColor= "black"
bgColor= "#778899"
text= ("Rockwell Extra Bold", 20)
pantalla.configure( bg= "#778899")
pantalla.geometry("650x650")

titleFrame= Frame(pantalla, bg= bgColor)
titleFrame.place(relwidth =1, relheight = 0.08)

Label(titleFrame, text= "Pantalla de Captura", font = text, anchor = CENTER, fg= fgColor, bg= bgColor).place(relx = .25, relheight=1)


matricula_entidad = Label(text= "MATRICULA: ", bg="#A9A9A9")
nombre_entidad = Label(text= "NOMBRE: ",bg="#A9A9A9")
apellido_entidad = Label(text= "APELLIDO: ",bg="#A9A9A9")
edad_entidad = Label(text= "EDAD: ",bg="#A9A9A9")
lugarnacimiento_entidad = Label(text= "LUGAR NACIMIENTO: ",bg="#A9A9A9")
estadocivil_entidad = Label(text= "ESTADO CIVIL: ",bg="#A9A9A9")
CP_entidad = Label(text= "CODIGO POSTAL: ",bg="#A9A9A9")
telefono_entidad = Label(text= "TELEFONO: ",bg="#A9A9A9")

matricula_entidad.place(x= 10, y=60)
nombre_entidad.place(x= 10, y = 120)
apellido_entidad.place(x= 10, y = 180)
edad_entidad.place(x= 10, y = 240)
lugarnacimiento_entidad.place(x= 10, y = 300)
estadocivil_entidad.place(x= 10, y = 360)
CP_entidad.place(x= 10, y = 420)
telefono_entidad.place(x= 10, y = 480)

matricula = IntVar()
nombre = StringVar()
apellido = StringVar()
edad = IntVar()
lugarnacimiento = StringVar()
estadocivil = StringVar()
CP = IntVar()
telefono = IntVar()

matricula_captura = Entry(textvariable = matricula, width="30")
nombre_captura = Entry(textvariable = nombre, width="30")
apellido_captura = Entry(textvariable = apellido, width="30")
edad_captura = Entry(textvariable = edad, width="30")
lugarnacimiento_captura = Entry(textvariable = lugarnacimiento, width="30")
estadocivil_captura = Entry(textvariable = estadocivil, width="30")
CP_captura = Entry(textvariable = CP, width="30")
telefono_captura = Entry(textvariable = telefono, width="30")


matricula_captura.place(x=10, y=80)
nombre_captura.place(x=10, y=140)
apellido_captura.place(x=10, y=200)
edad_captura.place(x=10, y=260)
lugarnacimiento_captura.place(x=10, y=320)
estadocivil_captura.place(x=10, y=380)
CP_captura.place(x=10, y=440)
telefono_captura.place(x=10, y=500)


guardar = Button(pantalla,text = "Guardar", width= "30", height = "2", command= guardar_dato, bg ="orange")
guardar.place(x=100, y= 560)

salir = Button(pantalla, text = "Salir", width = "30", height = "2", command= pantalla.destroy, bg="orange")
salir.place(x=340, y= 560)

pantalla.mainloop()