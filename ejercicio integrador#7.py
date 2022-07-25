def iniciarEjercicio_7():
    print("--- Ejercicio Retador #7 Diccionarios ---")

    clientes = {}

    while True:
        print("Menu principal")
        print("(1) Añadir cliente")
        print("(2) Listar todos los clientes")
        print("(3) Listar clientes preferentes")
        print("(4) Salir")
        opcion = input("Ingresa una opcion: ")

        if opcion == '1':
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

        elif opcion == '2':
            print("--- Listar todos los clientes ---")
            for cliente in clientes.items():
                print(cliente)
        elif opcion == '3':
            print("--- Listar clientes preferentes ---")
            for cliente in clientes.items():
                if cliente[1][3]:
                    print(cliente)
        elif opcion == '4':
            print("--- Saliste del programa ---")
            break

    iniciarEjercicio_7()
