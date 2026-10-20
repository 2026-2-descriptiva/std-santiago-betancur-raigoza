# def main():
#     """
#     Antes de limpiar o analizar un conjunto de datos, un analista debe
#     documentar qué problemas tiene. En este laboratorio usted no va a limpiar
#     `data/ventas.csv.gz`: va a construir un reporte de calidad que deje evidencia
#     de sus problemas, tal como están en el archivo.

#     Lea `data/ventas.csv.gz` sin modificar sus valores. Para trabajar con los
#     encabezados, normalícelos: páselos a minúsculas, elimine los espacios al
#     inicio y al final (y cualquier marca BOM) y reemplace los espacios
#     internos por `_`. Las columnas requeridas son `supplier_id`, `supplier`,
#     `country`, `city`, `purchase_date`, `amount`, `discount`, `weight`,
#     `units`, `unit_price` y `contact_email`.

#     Escriba el reporte en `submission/data_quality_report.json` con estas
#     claves:

#     - `row_count`: cantidad de filas de datos.
#     - `column_count`: cantidad de columnas.
#     - `missing_required_columns`: lista ordenada de columnas requeridas que no
#       están en el archivo.
#     - `unexpected_columns`: lista ordenada de columnas del archivo que no son
#       requeridas.
#     - `duplicate_row_count`: cantidad de filas idénticas a una fila anterior.
#     - `duplicate_supplier_id_row_count`: cantidad de filas cuyo `supplier_id`
#       aparece más de una vez (cuente todas esas filas, no solo las
#       repetidas).
#     - `missing_value_count_by_column`: diccionario con la cantidad de valores
#       faltantes de cada columna. Considere faltantes las celdas vacías y las
#       que contienen `N/A`.
#     - `invalid_email_count`: cantidad de valores de `contact_email` que no
#       tienen la forma `usuario@dominio.extension`.
#     - `invalid_unit_count`: cantidad de valores numéricos de `units` que no son
#       enteros positivos. Los valores faltantes no se cuentan aquí.
#     - `country_values`: lista ordenada de los valores distintos de `country`,
#       escritos exactamente como aparecen en el archivo.

#     La función también debe retornar el reporte como un diccionario.

#     Ejemplo del formato del reporte:

#         {
#           "row_count": 103,
#           "column_count": 11,
#           "missing_required_columns": [],
#           ...
#           "country_values": [" Colombia ", "CO", ...]
#         }
#     """

#     raise NotImplementedError
import json
import re
from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = [
    "supplier_id",
    "supplier",
    "country",
    "city",
    "purchase_date",
    "amount",
    "discount",
    "weight",
    "units",
    "unit_price",
    "contact_email",
]


def normalize_column_name(name):
    return re.sub(r"\s+", "_", name.lstrip("\ufeff").strip().lower())


def validate_required_columns(dataframe, required_columns):
    columns = set(dataframe.columns)
    required = set(required_columns)

    return {
        "missing_required_columns": sorted(required - columns),
        "unexpected_columns": sorted(columns - required),
    }


def build_quality_report(dataframe):
    structure = validate_required_columns(dataframe, REQUIRED_COLUMNS)

    email_pattern = r"[^@\s]+@[^@\s]+\.[^@\s]+"
    valid_email = dataframe["contact_email"].str.fullmatch(
        email_pattern, na=False
    )

    units = pd.to_numeric(dataframe["units"], errors="coerce")
    duplicate_supplier_ids = dataframe["supplier_id"].duplicated(keep=False)

    return {
        "row_count": int(len(dataframe)),
        "column_count": int(len(dataframe.columns)),
        **structure,
        "duplicate_row_count": int(dataframe.duplicated().sum()),
        "duplicate_supplier_id_row_count": int(duplicate_supplier_ids.sum()),
        "missing_value_count_by_column": {
            column: int(count)
            for column, count in dataframe.isna().sum().items()
        },
        "invalid_email_count": int((~valid_email).sum()),
        "invalid_unit_count": int(
            (units.notna() & ((units <= 0) | (units % 1 != 0))).sum()
        ),
        "country_values": sorted(
            dataframe["country"].dropna().unique().tolist()
        ),
    }


def main():
    root = Path(__file__).resolve().parents[1]

    source_file = root / "data" / "ventas.csv.gz"
    output_file = root / "submission" / "data_quality_report.json"

    dataframe = pd.read_csv(
        source_file,
        dtype="string",
        compression="gzip"
    )

    dataframe.columns = [
        normalize_column_name(column)
        for column in dataframe.columns
    ]

    report = build_quality_report(dataframe)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    output_file.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return report