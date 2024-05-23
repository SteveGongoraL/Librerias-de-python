import json                                     #with reserva recursos y los libera al terminar.
separador = ("°°°" * 40) + "\n"

diccionarioBase= {
    "cuentas":
        [
            {"cuenta":100, "nombre":"Steve", "saldo":9999},
            {"cuenta":200, "nombre":"Fernando", "saldo":9921},
            {"cuenta":300, "nombre":"Diana", "saldo":3428},
            {"cuenta":400, "nombre":"Krista", "saldo":2934},
            {"cuenta":500, "nombre":"Gaby", "saldo":1934}
        ]
    }

with open("cuentas.json", "w") as cuentasW:
    json.dump(diccionarioBase, cuentasW)

diccionarioBase = None     # El diccionario base deja de existir por el momento.

with open("cuentas.json", "r") as cuentasR:
    diccionarioBase = json.load(cuentasR)

print("Archivo completo en el diccionario")
print(diccionarioBase)
print(separador)

print("Diccionarios contenidos")
print(diccionarioBase["cuentas"])
print(separador)

print("Registro por registro")
for registro in diccionarioBase["cuentas"]:
    print(registro)
print(separador)
