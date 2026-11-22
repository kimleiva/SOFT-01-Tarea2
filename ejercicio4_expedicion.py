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