def buscar_valor(matriz, valor):
    # Recorrer la matriz para buscar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición si se encuentra el valor
    return None  # Retorna None si el valor no se encuentra

def main():
    # Definir una matriz 3x3
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Valor a buscar
    valor_a_buscar = 9

    # Llamar a la función de búsqueda
    resultado = buscar_valor(matriz, valor_a_buscar)

    # Mostrar el resultado
    if resultado:
        print(f"El valor {valor_a_buscar} se encontró en la posición {resultado}")
    else:
        print(f"El valor {valor_a_buscar} no se encontró en la matriz.")

if __name__ == "__main__":
    main()