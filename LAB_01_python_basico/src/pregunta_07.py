# def pregunta_07():
#     """
#     Para cada valor distinto de la segunda columna (`value`), construya la
#     lista de letras de la primera columna (`letter`) que aparecen con ese
#     valor. Conserve las letras repetidas y el orden en que aparecen en el
#     archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
#     valor.

#     Ejemplo del formato de la respuesta:

#         [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
#     """

#     raise NotImplementedError
import csv
import gzip
from pathlib import Path


def pregunta_07():
    """Asocia cada valor de la segunda columna con sus letras, preservando orden."""
    letters = {}

    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        for row in csv.reader(file, delimiter="\t"):
            letters.setdefault(int(row[1]), []).append(row[0])

    return sorted(letters.items())