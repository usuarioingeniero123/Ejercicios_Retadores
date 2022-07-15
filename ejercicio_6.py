from operator import itemgetter


def iniciarEjercicio_6():
    print("--- Ejercicio Retador #6 Operaciones de listas y tuplas ---")

    pasajeros = []

    while True:
        print("Ingresa (X) para salir del programa")
        nombre = input("Nombre: ")
        if nombre == 'X':
            break
        edad = input("Edad: ")
        codigoDestino = input("Destino: ")
        pasajeros.append((nombre, edad, codigoDestino))

    bjx = 0
    gdl = 0
    jal = 0
    edadPromedioBJX = 0
    edadPromedioGDL = 0
    edadPromedioJAL = 0
    detallesVuelos = []
    edadesPromedios = []

    for pasajero in pasajeros:
        if pasajero[2] == 'BJX':
            bjx += 1
            edadPromedioBJX += int(pasajero[1])
            edadPromedioBJX = edadPromedioBJX / bjx
        elif pasajero[2] == 'GDL':
            gdl += 1
            edadPromedioGDL += int(pasajero[1])
            edadPromedioGDL = edadPromedioGDL / gdl
        elif pasajero[2] == 'JAL':
            jal += 1
            edadPromedioJAL += int(pasajero[1])
            edadPromedioJAL = edadPromedioJAL / jal

    detallesVuelos.append(('BJX', bjx))
    detallesVuelos.append(('GDL', gdl))
    detallesVuelos.append(('JAL', jal))

    edadesPromedios.append(('BJX', edadPromedioBJX))
    edadesPromedios.append(('GDL', edadPromedioGDL))
    edadesPromedios.append(('JAL', edadPromedioJAL))

    print("Detalles de vuelos:")
    print(sorted(detallesVuelos, key=itemgetter(1), reverse=True))
    print("Edad promedio por vuelo:")
    print(sorted(edadesPromedios, key=itemgetter(1), reverse=True))
iniciarEjercicio_6()