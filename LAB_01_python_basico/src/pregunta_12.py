# def pregunta_12():
#     """
#     Para cada letra de la primera columna (`letter`), sume todos los valores
#     numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
#     Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

#     Ejemplo del formato de la respuesta:

#         {"A": 177, "B": 187, "C": 114, ...}
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_12():
    """Retorna la suma de los valores codificados en la quinta columna por letra."""
    totals = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            metric_total = sum(int(item.split(":")[1]) for item in row[4].split(","))
            totals[row[0]] = totals.get(row[0], 0) + metric_total

    return dict(sorted(totals.items()))