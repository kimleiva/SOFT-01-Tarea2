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
        
 # --- PROCESO ---
    agua_disponible = agua_disponible - agua_dia
    alimento_disponible = alimento_disponible - alimento_dia
    agua_consumida_total = agua_consumida_total + agua_dia
    alimento_consumido_total = alimento_consumido_total + alimento_dia
    jornadas_completadas = jornadas_completadas + 1

    print(f"Saldo restante: {agua_disponible} litros de agua y {alimento_disponible} unidades de alimento")

# --- SALIDA ---
promedio_agua = agua_consumida_total / jornadas_completadas
promedio_alimento = alimento_consumido_total / jornadas_completadas

if jornadas_completadas == jornadas_planeadas:
    estado = "Expedición completada"
else:
    estado = "Expedición interrumpida por agotamiento de recursos"

print("--- INFORME FINAL ---")
print(f"Jornadas planeadas: {jornadas_planeadas}")
print(f"Jornadas completadas: {jornadas_completadas}")
print(f"Agua consumida: {agua_consumida_total} litros")
print(f"Alimento consumido: {alimento_consumido_total} unidades")
print(f"Agua restante: {agua_disponible} litros")
print(f"Alimento restante: {alimento_disponible} unidades")
print(f"Promedio diario de agua: {promedio_agua} litros")
print(f"Promedio diario de alimento: {promedio_alimento} unidades")
print(f"Estado: {estado}")