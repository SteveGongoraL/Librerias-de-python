import openpyxl
separador = ("°°°" * 40) + "\n"

libro = openpyxl.load_workbook("MiArchivoExcel.xlsx")
print(type(libro))
nombre_hoja = libro.sheetnames[0]
print(f"El nombre de la hoja es: {nombre_hoja}")

# Imprimiendo valores por celda en especifico
hoja = libro[nombre_hoja]
valor_celda_A1 = hoja["A1"].value
valor_celda_B1 = hoja["B1"].value
print(f"El valor de la celda A1 es: {valor_celda_A1} \nEl valor de la celda B1 es: {valor_celda_B1}")
print(separador)

# Metodo por coordenada.
valor_celda_B1_coordenadas = hoja.cell(row=1, column=2).value
print(f"El valor que esta en la fila 1 columna 2 es: {valor_celda_B1_coordenadas}")
print(separador)

# Accesando a un rango de celdas.
print("Todos los valores de la columna 2")
for renglon in range(1,8,1):
    print(f"{renglon}, {hoja.cell(row=renglon, column=2).value}")
print(separador)


print("Imprimiendo todos los valores del archivo")
renago_celdas = hoja["A1":"C3"]
for Renglon in renago_celdas:
    for celda in Renglon:
        print(f"Celda: {celda.coordinate} = {celda.value}")
    print(" -- Fin del renglon -- ")
