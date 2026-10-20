# def pregunta_01():
#     """
#     El archivo `data/solicitudes_de_credito.csv.gz` contiene las solicitudes de
#     un programa de crédito, pero llegó sucio: tiene una columna de índice que
#     no pertenece a los datos, registros duplicados, registros incompletos y
#     valores que representan lo mismo escritos de formas distintas en los
#     campos de texto, las fechas, el estrato y el monto.

#     Su tarea es limpiarlo y guardar el resultado en
#     `submission/solicitudes_de_credito.csv`, usando punto y coma (`;`) como
#     separador y sin el índice de Pandas.

#     El archivo limpio debe cumplir lo siguiente:

#     - Contiene solamente las nueve columnas `sexo`, `tipo_de_emprendimiento`,
#       `idea_negocio`, `barrio`, `estrato`, `comuna_ciudadano`,
#       `fecha_de_beneficio`, `monto_del_credito` y `línea_credito`, en ese
#       orden.
#     - Los campos de texto están en minúsculas y sus palabras separadas por
#       espacios.
#     - `estrato` y `monto_del_credito` son números enteros, sin símbolos ni
#       separadores de miles.
#     - Todas las fechas de `fecha_de_beneficio` usan un mismo formato, por
#       ejemplo `AAAA-MM-DD`.
#     - No hay registros incompletos. La única excepción es
#       `comuna_ciudadano`: sus valores faltantes son parte de los datos
#       originales y deben conservarse.
#     - No hay registros duplicados.

#     Ejemplo del formato del archivo:

#         sexo;tipo_de_emprendimiento;idea_negocio;barrio;estrato;...
#         femenino;comercio;almacen de ropa en;los cerros el vergel;2;...
#         ...
#     """

#     raise NotImplementedError

from pathlib import Path
import pandas as pd


def pregunta_01():
    root = Path(__file__).resolve().parents[1]

    source_file = root / "data" / "solicitudes_de_credito.csv.gz"
    output_file = root / "submission" / "solicitudes_de_credito.csv"

    # Leer archivo comprimido
    df = pd.read_csv(
        source_file,
        sep=";",
        dtype="string",
        compression="gzip"
    )

    # Eliminar columna de índice accidental
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]

    # Normalizar campos categóricos
    categorical_columns = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "línea_credito",
    ]

    for column in categorical_columns:
        df[column] = (
            df[column]
            .str.replace("-", " ", regex=False)
            .str.strip()
            .str.lower()
        )

    # Normalizar estrato
    df["estrato"] = pd.to_numeric(
        df["estrato"],
        errors="coerce"
    ).astype("Int64")

    # Normalizar fechas
    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"].str.strip(),
        format="mixed",
        dayfirst=True,
        errors="coerce"
    ).dt.strftime("%d/%m/%Y")

    # Normalizar monto del crédito
    df["monto_del_credito"] = pd.to_numeric(
        df["monto_del_credito"]
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip(),
        errors="coerce"
    )

    # Eliminar registros con faltantes en campos requeridos
    df = df.dropna(
        subset=[
            "tipo_de_emprendimiento",
            "barrio",
        ]
    )

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Conservar las nueve columnas analíticas
    columns = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "barrio",
        "estrato",
        "comuna_ciudadano",
        "fecha_de_beneficio",
        "monto_del_credito",
        "línea_credito",
    ]

    df = df[columns]

    # Crear carpeta de salida
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Guardar archivo limpio
    df.to_csv(
        output_file,
        sep=";",
        index=False,
        encoding="utf-8"
    )

    return df


if __name__ == "__main__":
    pregunta_01()