# def pregunta_07():
#     """
#     Usando `data/tbl0.tsv`, sume los valores de la columna `c2` para cada
#     categoría de la columna `c1`. Retorne una Serie de Pandas cuyo índice son
#     las categorías, en orden alfabético, y cuyos valores son las sumas.

#     Ejemplo del formato de la respuesta:

#         c1
#         A    37
#         B    36
#         C    27
#         ...
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_07():
    """Retorne la suma de `c2` por cada categoría de `c1`."""
    path = Path(__file__).resolve().parents[1] / "data" / "tbl0.tsv"
    table = pd.read_csv(path, sep="\t")
    result = table.groupby("c1")["c2"].sum()
    result.name = None
    return result
    # raise NotImplementedError
