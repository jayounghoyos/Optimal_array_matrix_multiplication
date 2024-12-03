import sys


def matrix_chain_order(dimensions):
    # Obtiene la cantidad de matrices (n)
    n = len(dimensions) - 1
    # Inicializa la tabla min_cost para almacenar los costos mínimos de multiplicación
    min_cost = [[0] * n for _ in range(n)]
    # Tabla para almacenar los índices de partición óptimos
    partition_indices = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        # Recorre las subcadenas posibles de la longitud actual
        for i in range(n - length + 1):
            j = i + length - 1  # Índice final de la subcadena actual
            min_cost[i][
                j
            ] = sys.maxsize  # Inicializa con un valor grande para encontrar el mínimo
            # Prueba todas las posibles posiciones de partición en la subcadena (de i a j)
            for k in range(i, j):
                # Calcula el costo total de multiplicar la subcadena desde A_i hasta A_j
                cost = (
                    min_cost[i][k]
                    + min_cost[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )
                # Si encontramos un costo menor, actualizamos el costo mínimo en min_cost[i][j]
                if cost < min_cost[i][j]:
                    min_cost[i][j] = cost
                    partition_indices[i][j] = k
    return min_cost, partition_indices


def construct_optimal_order(partition_indices, i, j):
    # Construye la secuencia óptima de multiplicación utilizando la tabla de particiones
    if i == j:
        # Caso base: una sola matriz (no requiere paréntesis)
        return f"A{i+1}"
    k = partition_indices[i][j]  # Obtiene el índice de partición óptimo
    # Construye recursivamente la expresión para el lado izquierdo y derecho de la partición
    left_order = construct_optimal_order(partition_indices, i, k)
    right_order = construct_optimal_order(partition_indices, k + 1, j)
    return f"({left_order} x {right_order})"


def main():
    # Lee toda la entrada desde sys.stdin y la divide en líneas
    input = sys.stdin.read().strip().splitlines()
    case_number = 1  # contador de casos del input
    line_index = 0  # Índice para avanzar a través del input

    while line_index < len(input):
        # Lee el número de matrices en el caso actual
        n = int(input[line_index])
        line_index += 1
        if n == 0:
            break

        dimensions = []  # dimensiones por matriz
        for _ in range(n):
            # Lee las dimensiones las almacena en la lista
            rows, cols = map(int, input[line_index].split())
            dimensions.append(rows)  # Almacena el número de filas de la matriz actual
            line_index += 1
        dimensions.append(
            cols
        )  # Añade la última columna para completar la dimensión final

        # Calcula el orden óptimo de multiplicación y construye la expresión
        min_cost, partition_indices = matrix_chain_order(dimensions)
        optimal_order = construct_optimal_order(partition_indices, 0, n - 1)

        # Imprime el resultado para el caso actual
        print(f"Case {case_number}: {optimal_order}")
        case_number += 1


if __name__ == "__main__":
    main()
