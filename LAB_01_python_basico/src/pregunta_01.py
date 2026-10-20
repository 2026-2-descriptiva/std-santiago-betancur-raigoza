import csv
import gzip
from pathlib import Path

def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (value)
    del archivo data/data.csv.gz y retorne un número entero.
    """
    path = Path(__file__).resolve().parents[1] / "data" / "data.csv.gz"

    with gzip.open(path, "rt", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        return sum(int(row[1]) for row in reader)
    #raise NotImplementedError
