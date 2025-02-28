def bubble_sort(fila):
    """Ordena una fila utilizando el algoritmo Bubble Sort."""
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

def ordenar_fila_matriz(matriz, fila):
    """Ordena una fila específica de la matriz."""
    if fila < 0 or fila >= len(matriz):
        print("Fila no válida.")
        return
    # Copiar la fila para no modificar la original directamente
    fila_a_ordenar = matriz[fila].copy()
    bubble_sort(fila_a_ordenar)
    # Reemplazar la fila en la matriz con la fila ordenada
    matriz[fila] = fila_a_ordenar

def mostrar_matriz(matriz, mensaje):
    """Muestra la matriz en la consola."""
    print(mensaje)
    for fila in matriz:
        print(fila)

def main():
    # Definir una matriz 3x3
    matriz = [
        [9, 2, 5],
        [7, 1, 4],
        [3, 8, 6]
    ]

    # Mostrar la matriz original
    mostrar_matriz(matriz, "Matriz original:")

    # Fila a ordenar (índice basado en 0)
    fila_a_ordenar = 1

    # Ordenar la fila específica
    ordenar_fila_matriz(matriz, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    mostrar_matriz(matriz, f"\nMatriz con la fila {fila_a_ordenar} ordenada:")

if __name__ == "__main__":
    main()