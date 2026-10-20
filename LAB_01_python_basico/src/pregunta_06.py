# def pregunta_06():
#     """
#     La quinta columna (`metrics`) contiene pares `clave:valor` separados por
#     comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
#     aparecen en todo el archivo. Retorne una lista de tuplas
#     `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

#     Observe que el orden es mínimo y luego máximo, al contrario de la
#     pregunta 5.

#     Ejemplo del formato de la respuesta:

#         [("aaa", 1, 9), ("bbb", 1, 9), ...]
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_06():
    """Retorna mínimo y máximo de cada clave codificada en la quinta columna."""
    values = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            for item in row[4].split(","):
                key, value = item.split(":")
                values.setdefault(key, []).append(int(value))

    return [(key, min(group), max(group)) for key, group in sorted(values.items())]
