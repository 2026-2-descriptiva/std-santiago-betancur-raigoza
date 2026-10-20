# def pregunta_09():
#     """
#     Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
#     de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
#     claves en orden alfabético.

#     Ejemplo del formato de la respuesta:

#         {"aaa": 13, "bbb": 16, "ccc": 23, ...}
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_09():
    """Retorna la frecuencia de cada clave de la quinta columna."""
    counts = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            for item in row[4].split(","):
                key, _ = item.split(":")
                counts[key] = counts.get(key, 0) + 1

    return dict(sorted(counts.items()))