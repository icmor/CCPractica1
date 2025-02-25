"""Módulo para codificar gráficas como listas de adyacencias y matrices."""

from graph import adjacency_list, GraphL, GraphM
from math import ceil


def encode(graph: GraphL) -> str:
    """Codifica una gráfica como su lista de adyacencias con el esquema
    especificado. Los vértices están representados por números separados por
    comas y las vecindades están separadas por el símbolo '#'.
    """
    rows = []
    for neighbors in graph.adjlist:
        rows.append(",".join(str(vertex) for vertex in neighbors))
    return "#".join(rows)


def decode(coded_graph: str) -> GraphL:
    """Decodifica una gráfica como su lista de adyacencias con el esquema
    especificado. Los vértices están representados por números separados por
    comas y las vecindades están separadas por el símbolo '#'. La función
    devuelve un objeto GraphL.
    """
    adjlist: adjacency_list = []
    for neighbors in coded_graph.split("#"):
        if not neighbors:
            adjlist.append([])
        else:
            adjlist.append([int(vertex) for vertex in neighbors.split(",")])
    return GraphL(adjlist)


def encode_matrix(graph: GraphM) -> str:
    """Codificar una matriz de adyacencia en texto plano utilizando un alfabeto
    binario de unos y ceros. Los primeros ocho caracteres representan el orden
    de la gráfica en binario. Después se presenta la matriz como una secuencia
    de ceros y unos de longitud igual al número de vértices al cuadrado. Si los
    vértices i y j son adyacentes entonces la posición #vértices * i + j es
    igual a 1.
    """
    result = ""
    result += f"{graph.order:08b}" # codificamos el orden de la gráfica
    for row in range(graph.order):
        result += "".join("1" if graph.matrix[row][col] else "0"
                          for col in range(graph.order))
    return result


def decode_matrix(coded_graph: str) -> GraphM:
    """Decodificar una matriz de adyacencia en texto plano utilizando un
    alfabeto binario de unos y ceros. Los primeros ocho caracteres representan
    el orden de la gráfica en binario. Después se presenta la matriz como una
    secuencia de ceros y unos de longitud igual al número de vértices al
    cuadrado. Si los vértices i y j son adyacentes entonces la posición
    #vértices * i + j es igual a 1. Regresamos un objeto GraphM.
    """
    order = int(coded_graph[0:8], 2)
    print(order)
    matrix = []
    for i in range(8, order * (order + 1), order):
        matrix.append([1 if bit == "1" else 0
                       for bit in coded_graph[i:i+order]])
    return GraphM(matrix)
