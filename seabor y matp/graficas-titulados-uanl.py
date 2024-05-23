import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
separador = ("°°°" * 30) + "\n"
datos={"Año":("2015","2016","2017","2018","2019"), "Titulados": (12406,12885,17613,12469,16487)}

while True:
    print("""\n\nA continuación se representara el numero de estudiantes titulados de la UANL atravez de los años, mediante tres tipos de graficos.\n1)- Grafica de Barras.\n2)- Grafica de Lineas.\n3)- Grafica de Pastel.\n""")
    print(separador)
    opcion = int(input("¿Que opción deseas visualizar?: \nPon '0' Para salir.\n"))
    if opcion==0:
        break
    elif opcion == 1:
        print(f"Escogiste la opción {opcion} Grafica de Barras")
        sns.barplot(x="Año",y="Titulados",data=datos)
        plt.show()
    elif opcion ==2:
        print(f"Escogiste la opción {opcion} Grafica de Lineas")
        sns.relplot(x="Año",y="Titulados",data=datos,kind="line",color="#00da9d")
        plt.show()
    elif opcion ==3:
        print(f"Escogiste la opción {opcion} Grafica de Pastel")
        df=pd.DataFrame(datos)
        df.Titulados.groupby(df.Año).sum().plot(kind="pie",cmap="Spectral",autopct="%0.1f %%")
        plt.axis("equal")
        plt.show()
    else:
        print("Debes de elegir una opción válida.\n ")
else:
    print("Programa Terminado.")
