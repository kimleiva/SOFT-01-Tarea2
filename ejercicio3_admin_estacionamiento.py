# ==============================================================
# Archivo:     ejercicio3_admin_estacionamiento.py
# Autor:       Kimberly Leiva
# Curso:       SOFT-01 - Principios de Programación 1
# Fecha:       22/11/2026
# Ejercicio:   Administración de un estacionamiento privado
# Descripción: Sistema de consola para administrar un
#              estacionamiento de 20 espacios con tarifa de ₡800
#              por hora.
# ==============================================================

# --- CONSTANTES ---
ESPACIOS = 20
TARIFA_HORA = 800

# --- INICIALIZACIÓN ---
ocupacion_vehiculos = 0
salidas_registradas = 0
recaudacion_total = 0

# --- MENÚ PRINCIPAL ---
while True:
    print("--- ESTACIONAMIENTO ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupacion")
    print("4. Consultar recaudacion")
    print("5. Salir")
    opcion = input("Seleccione una opcion: ")

    # --- SELECCIÓN DE OPERACIÓN ---
    if opcion == "1":
        if ocupacion_vehiculos < ESPACIOS:
            ocupacion_vehiculos = ocupacion_vehiculos + 1
            espacios_libres = ESPACIOS - ocupacion_vehiculos
            print(f"Ingreso registrado. Espacios libres: {espacios_libres}")
        else:
            print("Estacionamiento lleno. No hay espacios disponibles.")
    elif opcion == "2":
        if ocupacion_vehiculos > 0:
            horas = int(input("Horas a cobrar: "))
            while horas <= 0:
                print("Error: ingrese un número entero mayor que cero.")
                horas = int(input("Horas a cobrar: "))
            pago = horas * TARIFA_HORA
            ocupacion_vehiculos = ocupacion_vehiculos - 1
            salidas_registradas = salidas_registradas + 1
            recaudacion_total = recaudacion_total + pago
            print(f"Salida registrada. Total a pagar: ₡{pago}")
        else:
            print("No hay vehículos en el estacionamiento.")
    elif opcion == "3":
        espacios_libres = ESPACIOS - ocupacion_vehiculos
        print(f"Espacios ocupados: {ocupacion_vehiculos}")
        print(f"Espacios libres: {espacios_libres}")
    elif opcion == "4":
        print(f"Recaudación total: ₡{recaudacion_total}")
        print(f"Vehículos que han salido: {salidas_registradas}")
    elif opcion == "5":
        espacios_libres = ESPACIOS - ocupacion_vehiculos
        print("\n--- RESUMEN FINAL ---")
        print(f"Vehículos dentro: {ocupacion_vehiculos}")
        print(f"Espacios libres: {espacios_libres}")
        print(f"Salidas registradas: {salidas_registradas}")
        print(f"Recaudación total: ₡{recaudacion_total}")
        break
    else:
        print("Error: opción no válida. Intente nuevamente.")
        