# def pregunta_11():
#     """
#     En `data/tbl1.tsv`, cada valor de la columna `c0` aparece en varias
#     filas, una por cada letra de la columna `c4`. Construya un DataFrame con
#     una fila por cada valor de `c0`, en orden ascendente, y las columnas `c0`
#     y `c4`. En `c4`, escriba las letras de ese `c0` ordenadas alfabéticamente
#     y separadas por comas.

#     Ejemplo del formato de la respuesta:

#             c0       c4
#         0    0    b,f,g
#         1    1    a,c,f
#         2    2  a,c,e,f
#         ...
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_11():
    """Retorne `tbl1` con los elementos de `c4` ordenados dentro de cada registro."""
    path = Path(__file__).resolve().parents[1] / "data" / "tbl1.tsv"
    table = pd.read_csv(path, sep="\t")
    result = table.groupby("c0", as_index=False).agg(list)
    result["c4"] = result["c4"].map(lambda values: ",".join(sorted(values)))
    return result[["c0", "c4"]]
    # raise NotImplementedError
