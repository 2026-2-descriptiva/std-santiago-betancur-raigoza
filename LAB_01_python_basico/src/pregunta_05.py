# def pregunta_05():
#     """
#     Para cada letra de la primera columna (`letter`), encuentre el valor
#     máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
#     de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

#     Ejemplo del formato de la respuesta:

#         [("A", 9, 2), ("B", 9, 1), ...]
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_05():
    """Retorna máximo y mínimo de la segunda columna por letra."""
    values = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            values.setdefault(row[0], []).append(int(row[1]))

    return [(letter, max(group), min(group)) for letter, group in sorted(values.items())]