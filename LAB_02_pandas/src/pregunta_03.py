# def pregunta_03():
#     """
#     Usando `data/tbl0.tsv`, cuente cuántos registros hay para cada categoría
#     de la columna `c1`. Retorne una Serie de Pandas cuyo índice son las
#     categorías, en orden alfabético, y cuyos valores son las cantidades.

#     Ejemplo del formato de la respuesta:

#         c1
#         A     8
#         B     7
#         C     5
#         ...
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_03():
    """Retorne la frecuencia de cada categoría de `c1`, ordenada alfabéticamente."""
    path = Path(__file__).resolve().parents[1] / "data" / "tbl0.tsv"
    table = pd.read_csv(path, sep="\t")
    result = table["c1"].value_counts().sort_index()
    result.name = None
    return result
    # raise NotImplementedError

