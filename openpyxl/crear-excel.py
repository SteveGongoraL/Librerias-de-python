import openpyxl
# Se encuentra en RAM hasta la linea 13.

libro= openpyxl.Workbook()
hoja= libro["Sheet"]
hoja.title="Primera"

hoja["B1"].value="Lista de numeros"
for renglon in range(2,12):
    hoja.cell(row=renglon, column=2).value = (renglon-1)
hoja["C12"].value = "=SUM(B2:B11)"

libro.save("MyExcelDesdePython.xlsx")
