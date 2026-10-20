# def pregunta_03():
#     """
#     Sume los valores de la segunda columna (`value`) para cada letra de la
#     primera columna (`letter`). Retorne una lista de tuplas `(letra, suma)`
#     ordenada alfabéticamente por la letra.

#     Ejemplo del formato de la respuesta:

#         [("A", 53), ("B", 36), ("C", 27), ...]
#     """

#     raise NotImplementedError

import csv
import gzip
from pathlib import Path


def pregunta_03():
    """Retorna la suma de la segunda columna por letra."""
    totals = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            totals[row[0]] = totals.get(row[0], 0) + int(row[1])

    return sorted(totals.items())