# ==============================================================
# Archivo:     ejercicio4_expedicion.py
# Autor:       Kimberly Leiva
# Curso:       SOFT-01 - Principios de Programación 1
# Fecha:       22/11/2026
# Versión:     1.0
# Ejercicio:   Control de abastecimiento de una expedición
# Descripción: Simula las jornadas de una expedición con 150
#              litros de agua y 100 unidades de alimento. Valida
#              la cantidad de jornadas (1 a 30) y los consumos
#              diarios, descuenta los recursos.
# ==============================================================

# --- CONSTANTES ---
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
JORNADAS_MINIMAS = 1
JORNADAS_MAXIMAS = 30

# --- INICIALIZACIÓN ---
agua_disponible = AGUA_INICIAL
alimento_disponible = ALIMENTO_INICIAL
agua_consumida_total = 0
alimento_consumido_total = 0
jornadas_completadas = 0

# --- ENTRADA: CANTIDAD DE JORNADAS ---
jornadas_planeadas = int(input("Cantidad de jornadas (1 a 30): "))
while jornadas_planeadas < JORNADAS_MINIMAS or jornadas_planeadas > JORNADAS_MAXIMAS:
    print("Error: la cantidad de jornadas debe estar entre 1 y 30.")
    jornadas_planeadas = int(input("Cantidad de jornadas (1 a 30): "))
    

# --- ITERACIÓN: JORNADAS ---
for jornada in range(1, jornadas_planeadas + 1):
    if agua_disponible == 0 or alimento_disponible == 0:
        break
    print(f"--- Jornada {jornada} ---")
    print(f"Disponible: {agua_disponible} litros de agua y {alimento_disponible} unidades de alimento")

    agua_dia = int(input("Agua consumida (litros): "))
    while agua_dia <= 0 or agua_dia > agua_disponible:
        print(f"Error: el consumo debe ser mayor que 0 y no superar {agua_disponible} litros.")
        agua_dia = int(input("Agua consumida (litros): "))

    alimento_dia = int(input("Alimento consumido (unidades): "))
    while alimento_dia <= 0 or alimento_dia > alimento_disponible:
        print(f"Error: el consumo debe ser mayor que 0 y no superar {alimento_disponible} unidades.")
        alimento_dia = int(input("Alimento consumido (unidades): "))