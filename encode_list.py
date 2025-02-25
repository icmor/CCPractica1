#!/usr/bin/env python3
"""Módulo para leer el orden y las aristas de una gráfica y escribir su lista
de adyacencias codificada a un archivo especificado.
"""

from graph import GraphL
from encoding import encode
import argparse
import pathlib
import sys


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lee una lista de aristas de INFILE y codifica su lista "
        "de adyacencias en OUTFILE.",
        epilog="La primera linea debe tener el orden de la gráfica. El resto "
        "de las líneas deben tener dos números separados por espacios que "
        "representan los extremos de una arista."
    )
    parser.add_argument("INFILE", type=pathlib.Path,
                        help="archivo donde leer la gráfica.")
    parser.add_argument("OUTFILE", type=pathlib.Path,
                        help="archivo donde escribir la gráfica codificada.")
    args = parser.parse_args()

    # leemos las aristas línea por línea
    lines = args.INFILE.read_text().split("\n")
    order = int(lines[0])
    adjlist = [[] for i in range(order)]
    for line in lines[1:]:
        if not line:
            continue
        try:
            v1, v2 = map(int, line.split())
            assert v1 <= order, f"Vértice {v1} fuera de rango!"
            assert v2 <= order, f"Vértice {v2} fuera de rango!"
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
        except ValueError:
            print("Los vértices deben ser dos números con al menos un espacio "
                  "entre ellos.")
            sys.exit(0)
    args.OUTFILE.write_text(encode(GraphL(adjlist)))
