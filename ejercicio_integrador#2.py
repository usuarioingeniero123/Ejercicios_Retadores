from dict_aeropuertos import datos
import operator


def iniciarEjercicioIntegrador():
    print("--- Ejercicio integrador Parte 2 ---")

    aeropuertos = []
    estados = datos['Estado']
    ciudades = datos['Ciudad']
    codigos = datos['Codigo_IATA']
    totalPasajeros = datos['Pasajeros']
    totalVuelos = datos['Vuelos_Sinaloa']

    totalPasajerosMaximos = []
    totalVuelosMenores = {}

    def organizarDatos():
        for n in range(0, len(estados)):
            aeropuertos.append({
                n: [estados[n], ciudades[n], codigos[n], totalPasajeros[n], totalVuelos[n]]
            })

    def mayoresPasajeros():
        indice = 0
        totalPasajerosTemporales = []
        for aeropuerto in aeropuertos:
            indice += 1
            totalPasajerosTemporales.append(aeropuerto[indice - 1][3])

        for n in range(0, 5):
            indice = 0
            totalPasajerosMaximo = max(totalPasajerosTemporales)
            for total in totalPasajerosTemporales:
                indice += 1
                if totalPasajerosMaximo == total:
                    totalPasajerosMaximos.append(totalPasajerosMaximo)
                    totalPasajerosTemporales.pop(indice - 1)

        print("[1] - Los 5 aeropuertos que tienen mayor cantidad de pasajeros que desean viajar a Sinaloa")
        for n in totalPasajerosMaximos:
            print(aeropuertos[totalPasajeros.index(n)])
        print("-------------------------------------------")

    def promedioPasajeros():
        indice = 0
        promedio = 0
        for aeropuerto in aeropuertos:
            indice += 1
            promedio += aeropuerto[indice - 1][3]

        promedio = int(promedio / indice)
        print("[2] - Promedio de pasajeros considerando todos los aeropuertos: " + str(promedio) + " pasajeros")
        print("-------------------------------------------")

    def menoresVuelos():
        indice = 0
        totalVuelosTemporales = {}
        for aeropuerto in aeropuertos:
            indice += 1
            if aeropuerto[indice - 1][4] != 0:
                totalVuelosTemporales[indice - 1] = aeropuerto[indice - 1][4]

        for n in range(0, 5):
            totalVuelosMenor = min(totalVuelosTemporales.items(), key=operator.itemgetter(1))
            totalVuelosMenores[totalVuelosMenor[0]] = totalVuelosMenor[1]
            totalVuelosTemporales.pop(totalVuelosMenor[0])

        print("[3] - Los 5 aeropuertos con menos vuelos hacia Sinaloa")
        for n in totalVuelosMenores:
            print(aeropuertos[n])
        print("-------------------------------------------")

    def promedioGeneral():
        for n in totalVuelosMenores:
            totalPasajerosMaximos.append(aeropuertos[n][n][3])

        indice = 0
        promedio = 0
        for total in totalPasajerosMaximos:
            indice += 1
            promedio += total

        promedio = int(promedio / indice)
        print("[4] - Promedio de pasajeros obtenidos según los puntos 1 y 3: " + str(promedio) + " pasajeros")
        print("-------------------------------------------")

    # Llamada a las funciones de los ejercicios.
    organizarDatos()
    mayoresPasajeros()
    promedioPasajeros()
    menoresVuelos()
    promedioGeneral()
