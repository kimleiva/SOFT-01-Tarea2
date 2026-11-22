# ==============================================================
# Nombre:      Kimberly Leiva
# Curso:       Ingenieria en Software - Principios de Programación 1
# Fecha:       22/11/2026
# Ejercicio:   Control de temperatura
# Descripción: Pide temperatura inicial, objetivo e incremento.
#              Valida que objetivo > inicial e incremento > 0.
#              Si es válido, un while sube la temperatura mientras
#              sea menor al objetivo, mostrando temperatura y ciclo.
# ==============================================================

# --- Entrada de datos ---
inicial = float(input("Temperatura inicial (°C): "))
objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

 #--- Validación ---
if objetivo <= inicial or incremento <= 0:
    print("Datos inválidos: El objetivo debe ser mayor que la temperatura inicial y el incremento debe ser mayor que 0.")
else:
    # --- Proceso ---
    temperatura = inicial
    ciclo = 0

    while temperatura < objetivo:
        temperatura += incremento
        ciclo += 1
        print(f"Ciclo: {ciclo}, Temperatura: {temperatura}")

