matrix = [
    [2, 1, 3],
    [3, 2, 1],
    [1, 2, 3]
]
opcion = 0
while opcion != 7:
    print("\nBienvenido al menú de matrices!, ¿qué quieres hacer? :)")
    print("1- Consultar Matriz")
    print("2- Consultar casilla por Columna y Fila")
    print("3- Insertar una fila")
    print("4- Eliminar una fila")
    print("5- Insertar un elemento")
    print("6- Eliminar un elemento")
    print("7- Salir")
    opcion = int(input("Selecciona tu opción :D "))
    # CONSULTAR MATRIZ
    if opcion == 1:
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    # CONSULTAR CASILLA
    elif opcion == 2:
        columnaConsulta = int(input("¿Qué columna vas a consultar? "))
        filaConsulta = int(input("¿Qué fila vas a consultar? "))
        print("El elemento es:", matrix[filaConsulta][columnaConsulta])
    # INSERTAR FILA
    elif opcion == 3:
        print("Cantidad de elementos que tendrá la nueva fila:",
              len(matrix[0]))
        filaVacia = []
        for i in range(len(matrix[0])):
            valor = input(f"Inserta el valor número {i}: ")
            filaVacia.append(valor)
        posicion = int(input("¿En qué posición quieres insertar la fila? "))
        matrix.insert(posicion, filaVacia)
        print("La matriz quedó como:")
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    # ELIMINAR FILA
    elif opcion == 4:
        for i, fila in enumerate(matrix):
            print(i, "-", fila)
        filaPorEliminar = int(input("¿Qué fila eliminarás? "))
        del matrix[filaPorEliminar]
        print("La matriz quedó como:")
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    # INSERTAR ELEMENTO
    elif opcion == 5:
        fila = int(input("¿En qué fila quieres insertar? "))
        columna = int(input("¿En qué columna quieres insertar? "))
        valor = input("¿Qué valor quieres insertar? ")
        matrix[fila].insert(columna, valor)
        print("La matriz quedó como:")
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    # ELIMINAR ELEMENTO
    elif opcion == 6:
        fila = int(input("¿De qué fila quieres eliminar un elemento? "))
        columna = int(input("¿Qué columna quieres eliminar? "))
        del matrix[fila][columna]
        print("La matriz quedó como:")
        for fila in matrix:
            for elemento in fila:
                print(elemento, end=" ")
            print()
    # SALIR
    elif opcion == 7:
        print("¡Hasta luego! :D")
    else:
        print("Opción no válida.")