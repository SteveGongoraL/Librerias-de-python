import time
separador = ("°°°" * 40) + "\n"
hora_inicial = time.time()
segundos_por_esperar = int(input("Cantidad de segundos a esperar:\n"))

# Esperando los segundos indicados por el usuario
time.sleep(segundos_por_esperar)
print(f"Han transcurrido, por lo menos {segundos_por_esperar} segundos.")
print(separador)

# Haciendo una prueba de tiempo
print("Iniciaremos la medición de un proceso simulado")
for termino in range(10):
    time.sleep(segundos_por_esperar)
print("¡Proceso simulado concluído!")
duracion_simulacro = time.time() - hora_inicial    # Puede afectar si cambias la hora del sistema.
print(f"La duración del proceso simulado fue de {duracion_simulacro} segundos.")
