import random 
M=int(input("Inserta la cantidad de columnas: "))
N=int(input("Inserta la cantidad de filas: "))
#M=random.randint(1,10)
#N=random.randint(1,10)
matriz= [[random.randint(1,10) for _ in range(N)] for _ in range(M)]
matriz2= [[random.randint(1,10) for _ in range(N)] for _ in range(M)]
for fila in matriz:
    print(fila)
print("")
for fila in matriz2:
    print(fila)

###MENU!!!!###

while True:

    print("\n----- MENU -----")
    print("1. Multiplicar la matriz por un escalar")
    print("2. Sumar dos matrices")
    print("3. Multiplicar dos matrices")
    print("4. Salir")

    opcion = int(input("Selecciona una opción: "))
    if opcion == 1:
        escalar = int(input("Inserta el escalar: "))
        resultado = []
        for fila in matriz:
            nueva_fila = []
            for numero in fila:
                nueva_fila.append(numero * escalar)
            resultado.append(nueva_fila)
        print("\nResultado:")
        for fila in resultado:
            print(fila)
    elif opcion == 2:
        resultado = []
        for i in range(M):
            fila = []
            for j in range(N):
                fila.append(matriz[i][j] + matriz2[i][j])
            resultado.append(fila)
        print("\nResultado:")
        for fila in resultado:
            print(fila)
    elif opcion == 3:
        if M != N:
            print("\nPara multiplicar estas matrices deben ser cuadradas.")
            print("Matriz 1:", M, "x", N)
            print("Matriz 2:", M, "x", N)
        else:
            resultado = []
            for i in range(M):
                fila = []
                for j in range(N):
                    total = 0
                    for k in range(N):
                        total += matriz[i][k] * matriz2[k][j]
                    fila.append(total)
                resultado.append(fila)
            print("\nResultado:")
            for fila in resultado:
                print(fila)
    elif opcion == 4:
        print("Programa terminado.")
        break
    else:
        print("Opción no válida.")




