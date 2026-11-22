# ==============================================================
# Nombre:      Kimberly Leiva
# Curso:       Ing
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
