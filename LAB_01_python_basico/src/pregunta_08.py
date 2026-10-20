# def pregunta_08():
#     """
#     Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
#     letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
#     tuplas `(valor, letras)` ordenada por el valor.

#     Ejemplo del formato de la respuesta:

#         [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_08():
    """Asocia cada valor de la segunda columna con letras únicas y ordenadas."""
    letters = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            letters.setdefault(int(row[1]), set()).add(row[0])

    return [(value, sorted(group)) for value, group in sorted(letters.items())]