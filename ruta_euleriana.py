"""Módulo para resolver los problemas planteados en el ejercicio 4:
- Encontrar el vértice con grado máximo de una gráfica
- Determinar si una gráfica tiene un camino euleriano
- Si una gráfica tiene un camino euleriano devolver dicho camino
"""

from graph import adjacency_matrix
from encoding import decode_matrix
import argparse
import pathlib


def get_max_degree(matrix: adjacency_matrix) -> (int, int):
    """Devuelve el vértice con mayor grado de una gráfica y su grado máximo."""
    max_degree = -1
    max_vertex = -1
    for vertex in range(len(matrix)):
        current_degree = sum(matrix[vertex])
        if current_degree > max_degree:
            max_degree = current_degree
            max_vertex = vertex
    return max_vertex, max_degree

def buscar_camino_euleriano(matriz_adyacencia):
    """Usa el algoritmo de Hierholzer para encontrar un camino euleriano en la grafica.

    Args:
        matriz_adyacencia (list of list of int): Matriz de adyacencia que representa la grafica.

    Returns:
        list: Camino euleriano si existe, de lo contrario None.
    """
    inicio, fin = -1, -1
    grados = [sum(fila) for fila in matriz_adyacencia]

    # Encuentra los vértices con grado impar
    for vertice, grado in enumerate(grados):
        if grado % 2 == 1:
            if inicio == -1:
                inicio = vertice
            elif fin == -1:
                fin = vertice
            else:
                return None

    # Si hay dos vértices impares, añadimos una arista ficticia para cerrar el ciclo
    if inicio != -1:
        matriz_adyacencia[inicio][fin] += 1
        matriz_adyacencia[fin][inicio] += 1
    else:
        # Busca el primer vértice no aislado para empezar
        inicio = next((i for i, grado in enumerate(grados) if grado > 0), -1)
        if inicio == -1:
            return []

    pila, camino = [inicio], []

    # Procesa cada vértice usando un recorrido en profundidad modificado
    while pila:
        vertice_actual = pila[-1]

        # Buscar una arista no utilizada
        siguiente = next((i for i, valor in enumerate(matriz_adyacencia[vertice_actual]) if valor > 0), None)

        if siguiente is None:
            # Añadir al camino si ya no tiene aristas
            camino.append(vertice_actual)
            pila.pop()
        else:
            # Usar arista y continuar al siguiente vértice
            matriz_adyacencia[vertice_actual][siguiente] -= 1
            matriz_adyacencia[siguiente][vertice_actual] -= 1
            pila.append(siguiente)

    if fin != -1:
        # Ajustar el camino para eliminar la arista ficticia
        for i in range(len(camino) - 1):
            if (camino[i] == inicio and camino[i + 1] == fin) or (camino[i] == fin and camino[i + 1] == inicio):
                camino = camino[i + 1:] + camino[1:i + 1]
                break

    # Verifique si quedan aristas, lo que indicaría que no hay camino euleriano debido a la falta de conexidad
    if any(sum(fila) > 0 for fila in matriz_adyacencia):
        return None

    return camino

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lee una gráfica codificada con su matriz de adyacencias en "
        "INFILE e imprime su orden, su tamaño, si contiene una ruta euleriana y "
        "si es el caso la sucesión de vértices de la ruta euleriana.")
    parser.add_argument("INFILE", type=pathlib.Path,
                    help="archivo donde leer la gráfica.")
    args = parser.parse_args()
    graph = decode_matrix(args.INFILE.read_text())

    # Imprime el número de vértices y aristas calculados
    print("Número de vértices:", graph.order)
    print("Número de aristas:", graph.size)

    max_vertex, max_degree = get_max_degree(graph.matrix)
    print("Vértice con grado máximo:", max_vertex)
    print("Grado máximo:", max_degree)

    # Intenta encontrar un camino euleriano y muestra el resultado
    camino_euleriano = buscar_camino_euleriano(graph.matrix)
    if camino_euleriano is None:
        print("¿La gráfica tiene un camino euleriano? NO")
    else:
        print("¿La gráfica tiene un camino euleriano? SI")
        print("El camino euleriano es:", *camino_euleriano)
