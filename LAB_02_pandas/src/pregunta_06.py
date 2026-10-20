# def pregunta_06():
#     """
#     Usando `data/tbl1.tsv`, obtenga los valores distintos de la columna `c4`,
#     conviértalos a mayúsculas y retórnelos como una lista ordenada
#     alfabéticamente.

#     Ejemplo del formato de la respuesta:

#         ["A", "B", "C", "D", "E", "F", "G"]
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_06():
    """Retorne valores únicos de `c4` en mayúsculas y ordenados alfabéticamente."""
    path = Path(__file__).resolve().parents[1] / "data" / "tbl1.tsv"
    table = pd.read_csv(path, sep="\t")
    return sorted(table["c4"].str.upper().unique().tolist())
    # raise NotImplementedError
