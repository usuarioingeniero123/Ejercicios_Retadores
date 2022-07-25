import csv
import operator


def iniciarSynergy():
    archivo = open("synergy_logistics_database.csv")
    lector = csv.reader(archivo)

    indice = 0
    BD = {}
    for fila in lector:
        if fila[4] == '2015':
            indice += 1
            BD[indice] = fila

    rutas = []
    for fila in BD.items():
        ruta = fila[1][2] + ' - ' + fila[1][3]
        if ruta not in rutas:
            rutas.append(ruta)

    serviciosRutas = {}
    for ruta in rutas:
        servicios = []
        for servicio in BD.items():
            if ruta == servicio[1][2] + ' - ' + servicio[1][3]:
                servicios.append(servicio)
                serviciosRutas[ruta] = servicios

    totalesMaximosServicios = {}
    for servicios in serviciosRutas.items():
        totalesServicios = {}
        for servicio in servicios[1]:
            totalesServicios[servicio[0]] = servicio[1][9]
        totalMaximo = max(totalesServicios.items(), key=operator.itemgetter(1))
        totalesMaximosServicios[totalMaximo[0]] = totalMaximo[1]

    for n in range(0, len(totalesMaximosServicios)):
        if n + 1 <= 64:
            totalMinimo = min(totalesMaximosServicios.items(), key=operator.itemgetter(1))
            totalesMaximosServicios.pop(totalMinimo[0])

    print("-------------------------------------------")
    print("Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más demandadas.")
    print("Acorde a los flujos tanto de importación como de exportación, indica:")
    print("¿Cuáles son esas 10 rutas?")
    print("-------------------------------------------")
    for totalServicio in totalesMaximosServicios.items():
        print(BD[totalServicio[0]])
