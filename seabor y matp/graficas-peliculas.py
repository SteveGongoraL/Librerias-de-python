import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
separador = ("°°°" * 40) + "\n"
datos=pd.read_csv('movies.csv')
df=pd.DataFrame(datos)

while True:
    print("MENU de opciones: ")
    print("1)- Genero de pelicula con mas Likes(plt).\n2)- Promedio de ganancia(plt).\n3)- Comparar el presupuesto(plt).\n4)- Pelicula con mas likes(sns).\n5)- Comparar ganacias(sns).\n6)- Comparar generos(sns).\n7)- Comparar los likes por año(sns).\n8)- Comprobar likes agrupado en clasificacion(sns).\n9)- Salir.\n ")
    print(separador)
    opcion = input("¿Que operacion deseas realizar?: \n")
    plt.figure(figsize=(11, 6))
    if opcion == "1":
        print("Grafica para ver que genero de pelicula obtuvo mas likes en facebook.\n")
        print(separador)
        df.groupby('genres')['movie_facebook_likes'].sum().plot(kind='barh',legend='Reverse',color="green")
        plt.xlabel("Suma de likes")
        plt.subplots_adjust(left=0.270)
        plt.show()
    elif opcion =="2":
        print("Grafica para ver el promedio de ganancias.\n")
        print(separador)
        df.gross.groupby(df.genres).mean().plot(kind='pie',cmap="Paired")
        plt.axis("equal")
        plt.ylabel("")
        plt.title("Promedio de ganancias")
        plt.show()
    elif opcion =="3":
        print("Grafica para comparar el presupuesto con la calificacion de la pelicula.\n")
        print(separador)
        df.groupby('budget')['imdb_score'].sum().plot(kind='bar',legend='Reverse',color="Black")
        plt.xlabel("Presupuesto")
        plt.ylabel("Calificación")
        plt.subplots_adjust(bottom=0.210)
        plt.show()
    elif opcion =="4":
        print("Grafica de Dispercion para ver la pelicula con mas likes.\n")
        print(separador)
        sns.lmplot(x="num",y="movie_facebook_likes",data=df,fit_reg=False,hue="num",legend=False,palette="Paired")
        plt.xlabel("Pelicula")
        plt.ylabel("Likes de la pelicula")
        plt.show()
    elif opcion =="5":
        print("Grafica para comparar ganancias con la calificacion de la pelicula.\n")
        print(separador)
        g=sns.lmplot(x="gross",y="imdb_score",data=df,palette="Set1")
        plt.show()
    elif opcion =="6":
        print("Grafica para comparar generos con los likes de facebook, calificacion y ganancias.\n")
        print(separador)
        nuevo=df[["genres","movie_facebook_likes","gross","imdb_score"]]
        sns.set(style="ticks",color_codes=True)
        g=sns.pairplot(nuevo,hue="genres",palette="Spectral")
        plt.show()
    elif opcion =="7":
        print("Graficas para comparar los likes por año de cada pelicula.\n")
        print(separador)
        g=sns.lmplot(x="imdb_score",y="movie_facebook_likes",data=df,hue="num",col="title_year",aspect=.4,x_jitter=0.1)
        plt.show()
    elif opcion =="8":
        print("Grafica para comparar la clasificacion de la pelicula con likes y ganancias.\n")
        print(separador)
        g=sns.lmplot(x="gross",y="movie_facebook_likes",hue="content_rating",data=df,palette="Set1")
        plt.show()
    elif opcion =="9":
        break
    else:
        print("Debes de elegir una opción valida\n ")
else:
    print("Programa Terminado.")
