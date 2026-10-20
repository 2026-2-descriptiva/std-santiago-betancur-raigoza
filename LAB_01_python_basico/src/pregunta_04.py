# def pregunta_04():
#     """
#     Cuente cuántos registros hay en cada mes, usando la fecha de la tercera
#     columna (`date`). Represente el mes como un texto de dos dígitos y retorne
#     una lista de tuplas `(mes, cantidad)` ordenada por el mes.

#     Ejemplo del formato de la respuesta:

#         [("01", 3), ("02", 4), ("03", 2), ...]
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_04():
    """Retorna la cantidad de registros por mes."""
    counts = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            month = row[2][5:7]
            counts[month] = counts.get(month, 0) + 1

    return sorted(counts.items())
