#!/usr/bin/env python3
"""Módulo para leer una gráfica codificada como lista en un archivo y
escribirla codificada como matriz en otro archivo.
"""

import argparse
import pathlib
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lee una matriz codificada de INFILE y codifica su matriz "
        "de adyacencias en OUTFILE.",
    )
    parser.add_argument("INFILE", type=pathlib.Path,
                        help="archivo donde leer la gráfica codificada.")
    parser.add_argument("OUTFILE", type=pathlib.Path,
                        help="archivo donde escribir la matriz codificada.")
    args = parser.parse_args()
    text = args.INFILE.read_text()

    # obtenemos el orden de la gráfica
    order = text.count("#") + 1
    # creamos un arreglo que representa a la matriz de adyacencias
    matrix = ["0"] * order * order
    for row, neighbors in enumerate(text.split("#")):
        if not neighbors:
            continue
        for vertex in neighbors.split(","):
            matrix[row * order + int(vertex)] = "1"
    result = f"{order:08b}" + "".join(matrix)
    args.OUTFILE.write_text(result)
