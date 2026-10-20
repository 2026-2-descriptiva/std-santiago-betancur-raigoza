# import pandas as pd
#
#
# def build_cohort_analysis() -> pd.DataFrame:
#     """
#     Una tienda quiere saber si sus clientes vuelven a comprar después de su
#     primera compra. Para responder, agrupe a los clientes en cohortes según
#     el mes de su primera compra y mida, mes a mes, qué proporción de cada
#     cohorte vuelve a comprar. Use `data/sales.csv.gz`, que tiene una fila por
#     orden con su cliente (`CustomerID`) y su fecha (`OrderDate`).
#
#     Use estas definiciones:
#
#     - `cohort_month`: el mes de la primera compra del cliente, escrito como
#       `AAAA-MM`.
#     - `period_index`: los meses transcurridos desde `cohort_month`; es 0 en el
#       mes de la primera compra, 1 en el mes siguiente, y así sucesivamente.
#     - `active_customers`: la cantidad de clientes distintos de la cohorte que
#       compraron en ese período.
#     - `cohort_size`: la cantidad de clientes de la cohorte, es decir, sus
#       clientes activos en el período 0.
#     - `retention_rate`: `active_customers` sobre `cohort_size`.
#
#     Genere dos archivos en `submission/`:
#
#     1. `cohort_retention.csv`, sin el índice de Pandas, con las columnas
#        `cohort_month`, `period_index`, `active_customers`, `cohort_size` y
#        `retention_rate`, y una fila por cada combinación cohorte–período
#        observada, ordenadas por cohorte y período.
#
#     2. `cohort_retention_heatmap.png`, un mapa de calor de `retention_rate`
#        con una fila por cohorte (eje vertical) y una columna por período
#        (eje horizontal). Muestre los valores como porcentajes. Los períodos
#        que todavía no se pueden observar para una cohorte no significan
#        retención cero: déjelos vacíos en el mapa.
#
#     La función también debe retornar la tabla de retención.
#
#     Ejemplo del formato de `cohort_retention.csv`:
#
#         cohort_month,period_index,active_customers,cohort_size,retention_rate
#         2022-01,0,100,100,1.0
#         2022-01,1,26,100,0.26
#         ...
#     """
#
#     raise NotImplementedError

from pathlib import Path

import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.ticker import PercentFormatter


def build_cohort_analysis() -> pd.DataFrame:
    """Calcula la retencion mensual y genera su mapa de calor."""
    activity_dir = Path(__file__).resolve().parents[1]
    data = pd.read_csv(activity_dir / "data" / "sales.csv.gz")
    data["order_month"] = pd.to_datetime(data["OrderDate"]).dt.to_period("M")
    data["cohort_month"] = data.groupby("CustomerID")["order_month"].transform("min")
    data["period_index"] = (
        (data["order_month"].dt.year - data["cohort_month"].dt.year) * 12
        + data["order_month"].dt.month - data["cohort_month"].dt.month
    )
    retention = (
        data.groupby(["cohort_month", "period_index"])["CustomerID"]
        .nunique()
        .rename("active_customers")
        .reset_index()
        .sort_values(["cohort_month", "period_index"])
        .reset_index(drop=True)
    )
    cohort_sizes = retention.loc[retention["period_index"] == 0].set_index(
        "cohort_month"
    )["active_customers"]
    retention["cohort_size"] = retention["cohort_month"].map(cohort_sizes)
    retention["retention_rate"] = (
        retention["active_customers"] / retention["cohort_size"]
    )
    retention["cohort_month"] = retention["cohort_month"].astype(str)

    submission_dir = activity_dir / "submission"
    submission_dir.mkdir(parents=True, exist_ok=True)
    retention.to_csv(submission_dir / "cohort_retention.csv", index=False)

    # El pivote conserva como NaN los periodos sin observaciones.
    matrix = retention.pivot(
        index="cohort_month", columns="period_index", values="retention_rate"
    )
    fig = Figure(figsize=(10, 6), layout="constrained")
    FigureCanvasAgg(fig)
    ax = fig.subplots()
    image = ax.imshow(matrix.to_numpy(), cmap="Blues", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(len(matrix.columns)), labels=matrix.columns)
    ax.set_yticks(range(len(matrix.index)), labels=matrix.index)
    ax.set_xlabel("Meses desde la primera compra")
    ax.set_ylabel("Mes de la cohorte")
    ax.set_title("Retencion de clientes por cohorte")
    for row in range(len(matrix.index)):
        for column in range(len(matrix.columns)):
            value = matrix.iloc[row, column]
            if pd.notna(value):
                ax.text(
                    column, row, f"{value:.0%}", ha="center", va="center",
                    color="white" if value > 0.5 else "black",
                )
    fig.colorbar(image, ax=ax, format=PercentFormatter(xmax=1), label="Retencion")
    fig.savefig(submission_dir / "cohort_retention_heatmap.png", dpi=150)
    return retention


if __name__ == "__main__":
    build_cohort_analysis()
