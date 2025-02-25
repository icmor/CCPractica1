"""Clases para representar y manipular gráficas."""

from pprint import pformat
from typing import Self


adjacency_list = list[list[int]]
adjacency_matrix = list[int]


class GraphL:
    """Clase para representar un grafo utilizando su lista de adyacencia."""
    def __init__(self, adjlist: adjacency_list) -> None:
        self.adjlist = adjlist

    def __len__(self) -> int:
        """Obtiene el orden de la gráfica."""
        return len(self.adjlist)

    @property
    def order(self) -> int:
        """Obtiene el orden de la gráfica."""
        return len(self)

    @property
    def size(self) -> int:
        """Obtiene el tamaño de la gráfica."""
        return sum(len(neighbors) for neighbors in self.adjlist)

    def __repr__(self) -> str:
        return str(self.adjlist)

    def __str__(self) -> str:
        return pformat(self.adjlist)


class GraphM:
    """Clase para representar un grafo utilizando su matriz de adyacencia."""
    def __init__(self, matrix: adjacency_matrix) -> None:
        self.matrix = matrix

    @staticmethod
    def from_GraphL(graph: GraphL) -> Self:
        matrix = [[0 for j in range(graph.order)] for i in range(graph.order)]
        for row, neighbors in enumerate(graph.adjlist):
            for vertex in neighbors:
                assert vertex <= graph.order, f"{vertex} está fuera de rango."
                matrix[row][vertex] = 1
        return GraphM(matrix)
    
    def __len__(self) -> int:
        """Obtiene el orden de la gráfica."""
        return len(self.matrix)

    @property
    def order(self) -> int:
        """Obtiene el orden de la gráfica."""
        return len(self)

    @property
    def size(self) -> int:
        """Obtiene el tamaño de la gráfica."""
        return sum(sum(neighbors) for neighbors in self.matrix)

    def __repr__(self) -> str:
        return str(self.matrix)

    def __str__(self) -> str:
        return pformat(self.matrix)
