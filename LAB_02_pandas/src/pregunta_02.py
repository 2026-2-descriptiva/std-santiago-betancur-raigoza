# def pregunta_02():
#     """
#     ¿Cuántas columnas tiene la tabla `data/tbl0.tsv`? Retorne la cantidad
#     como un número entero.

#     Ejemplo del formato de la respuesta:

#         4
#     """

#     raise NotImplementedError
import pandas as pd
from pathlib import Path


def pregunta_02():
    """Retorne la cantidad de columnas de `tbl0.tsv`."""
    path = Path(__file__).resolve().parents[1] / "data" / "tbl0.tsv"
    table = pd.read_csv(path, sep="\t")
    return len(table.columns)
    # raise NotImplementedError
