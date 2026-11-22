# ==============================================================
# Nombre:      Kimberly Leiva
# Curso:       Ingenieria en Software - Principios de Programación 1
# Fecha:       22/11/2026
# Ejercicio:   Registro de consumo de agua
# Descripción: Registra el consumo de agua de siete días con un
#               ciclo for. Calcula el total, el promedio, el mayor
#               consumo y los días que superan 150 litros.
# ==============================================================

# --- CONSTANTES ---
DIAS_SEMANA = 7
UMBRAL_LITROS = 150

# --- Inicializacion ---
consumo_total = 0
dias_sobre_umbral = 0
consumo_maximo = 0

# --- Iteración ---
for dia in range(1, DIAS_SEMANA + 1):
    consumo_dia = float(input(f"Día {dia} - Consumo de agua (litros): ")) 
    while consumo_dia < 0:
        print("Error: el consumo no puede ser negativo.")
        consumo_dia = float(input(f"Día {dia} - Consumo de agua (litros): "))
        print(consumo_dia)  # temporal: se elimina en pasos posteriores
        