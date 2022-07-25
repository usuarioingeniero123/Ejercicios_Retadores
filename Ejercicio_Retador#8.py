#Ejercicio retador #8
#Funciones en Python
def iniciarEjercicio_8():
    print("--- Ejercicio Retador #8 Funciones en Python ---")

    clientes = {
        '45471': ['Luis Perez', 45, 'BJX', True],
        '8944411': ['Fernanda Garcia', 25, 'JAL', True],
        '15223': ['Alejandra Ortiz', 33, 'JDL', True]
    }

    def agregarCliente():
        print("--- Añadir cliente ---")
        ine = input("Ingresa el ID del INE: ")
        nombre = input("Ingresa el Nombre: ")
        edad = input("Ingresa la edad: ")
        codigoDestino = input("Ingresa el destino: ")
        clientePreferente = input("Cliente preferente (Si/NO): ")

        clientes[ine] = [
            nombre,
            edad,
            codigoDestino,
            clientePreferente == 'Si' if True else False
        ]

    def listarClientes():
        print("--- Listar todos los clientes ---")
        for cliente in clientes.items():
            print(cliente)
        print("-------------------------------------------")

    def listarClientesPreferentes():
        print("--- Listar clientes preferentes ---")
        for cliente in clientes.items():
            if cliente[1][3]:
                print(cliente)
        print("-------------------------------------------")

    def eliminarCliente():
        print("--- Eliminar un cliente mediante ID del INE ---")
        ine = input("Ingrese INE del cliente a eliminar: ")
        del clientes[ine]
        for cliente in clientes.items():
            print(cliente)
        print("[ok] Cliente eliminado")
        print("-------------------------------------------")

    def edadPromedioClientes():
        print("--- Edad promedio de todos los clientes ---")
        edadPromedio = 0
        for cliente in clientes.items():
            edadPromedio += int(cliente[1][1])
        edadPromedio = edadPromedio / len(clientes)
        print("La edad promedio de todos los clientes es: " + str(edadPromedio))
        print("-------------------------------------------")

    def edadPromedioClientesPreferentes():
        print("--- Edad promedio de clientes preferentes ---")
        edadPromedio = 0
        for cliente in clientes.items():
            if cliente[1][3]:
                edadPromedio += int(cliente[1][1])
        edadPromedio = edadPromedio / len(clientes)
        print("La edad promedio de todos los clientes preferentes es: " + str(edadPromedio))
        print("-------------------------------------------")

    while True:
        print("Menu principal")
        print("(1) Añadir cliente")
        print("(2) Listar todos los clientes")
        print("(3) Listar clientes preferentes")
        print("(4) Eliminar un cliente mediante ID del INE")
        print("(5) Edad promedio de todos los clientes")
        print("(6) Edad promedio de clientes preferentes")
        print("(7) Salir")
        opcion = input("Ingresa una opcion: ")

        if opcion == '1':
            agregarCliente()
        elif opcion == '2':
            listarClientes()
        elif opcion == '3':
            listarClientesPreferentes()
        elif opcion == '4':
            eliminarCliente()
        elif opcion == '5':
            edadPromedioClientes()
        elif opcion == '6':
            edadPromedioClientesPreferentes()
        elif opcion == '7':
            print("--- Saliste del programa ---")
            break

iniciarEjercicio_8()
