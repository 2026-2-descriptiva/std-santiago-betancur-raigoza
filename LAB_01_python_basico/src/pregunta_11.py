# def pregunta_11():
#     """
#     La cuarta columna (`codes`) contiene letras minúsculas separadas por
#     comas. Para cada una de esas letras, sume los valores de la segunda
#     columna (`value`) de los registros en los que aparece. Retorne un
#     diccionario `{letra: suma}` con las letras en orden alfabético.

#     Ejemplo del formato de la respuesta:

#         {"a": 122, "b": 49, "c": 91, ...}
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_11():
    """Retorna la suma de la segunda columna por código de la cuarta columna."""
    totals = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            for code in row[3].split(","):
                totals[code] = totals.get(code, 0) + int(row[1])

    return dict(sorted(totals.items()))