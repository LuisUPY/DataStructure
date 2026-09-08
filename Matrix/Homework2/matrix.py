matrix = [
    [2, 1, 3],
    [3, 2, 1],
    [1, 2, 3]
]
#        columnas
#       0  1  2
## #   ┌─────────
#fila 0│ 1  2  3
#fila 1│ 4  5  6
#fila 2│ 7  8  9

opcion=0
while opcion !=7:
#opcion = int(input("Selecciona tu opción :D "))
    if opcion !=7:
        print("Bienvenido al menú de matrices!, que quieres hacer? :)")
        print("1- Consultar Matriz: ")
        print("2- Consultar casilla por Columna y Fila: ")
        print("3- Insertar una fila")
        print("4- Eliminar una fila")
        print("5- Insertar un elemento")
        print("6- Eliminar un elemento")
        print("7- Salir")

        opcion = int(input("Selecciona tu opción :D "))
        if opcion == 1:
            for fila in matrix:
                for elemento in fila:
                    print(elemento, end=" ")
                print()
        elif opcion == 2:
            ColumnaConsulta= input("Que Columna vas a consultar? ")
            FilaConsulta= ("Que Fila vas a consultar? ")
            print(matrix[ColumnaConsulta][FilaConsulta])
        elif opcion ==3:
            print(f"Cantidad de elementos que tienes que insertar: ", len(matrix))
            filavacia = []
            for i in range(len(matrix[0])):
                valor=input(f"Inserta el valor número {i}: ")
                filavacia.append(valor)
            matrix.append(filavacia)
        elif opcion == 4:
            for fila in matrix:
                            for elemento in fila:
                                print(elemento, end=" ")
                            print()
            filaporeliminar= int(input("¿Que fila eliminarás?"))
            del matrix[filaporeliminar]
            print("La matriz quedaría como: ")
            for fila in matrix:
                                        for elemento in fila:
                                            print(elemento, end=" ")
                                        print()