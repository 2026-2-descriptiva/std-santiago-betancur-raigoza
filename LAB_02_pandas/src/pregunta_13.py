# def pregunta_13():
#     """
#     Combine las tablas `data/tbl0.tsv` y `data/tbl2.tsv` usando la columna
#     `c0`, que ambas comparten. Luego, sume los valores de la columna `c5b`
#     para cada categoría de la columna `c1`. Retorne una Serie de Pandas cuyo
#     índice son las categorías, en orden alfabético, y cuyos valores son las
#     sumas.

#     Ejemplo del formato de la respuesta:

#         c1
#         A    146
#         B    134
#         C     81
#         ...
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_13():
    """Una `tbl0` y `tbl2` por `c0` y retorne la suma de `c5b` por `c1`."""
    data_dir = Path(__file__).resolve().parents[1] / "data"
    left = pd.read_csv(data_dir / "tbl0.tsv", sep="\t")
    right = pd.read_csv(data_dir / "tbl2.tsv", sep="\t")
    result = left.merge(right, on="c0").groupby("c1")["c5b"].sum()
    result.name = None
    return result
    # raise NotImplementedError

