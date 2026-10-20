# import pandas as pd
#
#
# def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
#     """
#     Una entidad pública recibe peticiones, quejas, reclamos y sugerencias
#     (PQRS) por dos canales, la página web y las cartas, y la ley le da 15 días
#     hábiles para responder cada una. Su tarea es medir si la entidad cumple
#     ese plazo.
#
#     Los archivos `data/historical_requests_web.csv.gz` y
#     `data/historical_requests_letter.csv.gz` tienen una fila por solicitud
#     recibida entre 2016 y 2021 por cada canal, con su identificador
#     (`record_id`), la fecha de entrada (`in_date`), el día de la semana de
#     entrada (`day_name`) y la fecha de respuesta (`out_date`). Si `out_date`
#     está vacía, la solicitud todavía no ha sido respondida.
#
#     Tenga en cuenta lo siguiente:
#
#     - Algunas solicitudes aparecen repetidas: elimine las filas idénticas
#       dentro de cada canal, para contar cada solicitud una sola vez. Las
#       filas sin `record_id` son solicitudes válidas.
#     - Llame `letter` al canal de las cartas y `web` al de la página web.
#     - Los días hábiles de respuesta son los días de lunes a viernes
#       posteriores a la fecha de entrada, hasta la fecha de respuesta
#       incluida. Por ejemplo, una solicitud que entra un viernes y se responde
#       el lunes siguiente tardó 1 día hábil. No considere los festivos.
#     - Los días calendario de respuesta son la diferencia entre la fecha de
#       respuesta y la de entrada.
#     - Una solicitud cumple el plazo si fue respondida en 15 días hábiles o
#       menos. Una solicitud pendiente no ha cumplido el plazo.
#     - `on_time_rate` es la proporción de solicitudes que cumplen el plazo,
#       sobre el total de solicitudes, incluidas las pendientes.
#     - Las medianas de días se calculan solamente con las solicitudes
#       respondidas.
#
#     Genere tres archivos en `submission/`, sin el índice de Pandas y con las
#     columnas en el orden indicado:
#
#     1. `channel_summary.csv`, con una fila por canal, en orden alfabético:
#        `channel`, `requests`, `answered`, `pending`,
#        `median_business_days` y `on_time_rate`.
#
#     2. `yearly_summary.csv`, con una fila por año de entrada y canal,
#        ordenada por año y luego por canal: `year`, `channel`, `requests`,
#        `pending` y `on_time_rate`.
#
#     3. `entry_day_summary.csv`, con una fila por día de entrada, de lunes a
#        domingo, con los dos canales juntos: `day_name`, `requests`,
#        `median_calendar_days` y `median_business_days`.
#
#     Observe en el tercer archivo cómo cambia la lectura del tiempo de
#     respuesta según se cuenten días calendario o días hábiles.
#
#     La función también debe retornar las tres tablas, en el mismo orden.
#
#     Ejemplo del formato de `channel_summary.csv`:
#
#         channel,requests,answered,pending,median_business_days,on_time_rate
#         letter,28138,...
#         ...
#     """
#
#     raise NotImplementedError


from pathlib import Path

import numpy as np
import pandas as pd


def pregunta_01() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Resume los tiempos y el cumplimiento de las solicitudes por canal."""
    activity_dir = Path(__file__).resolve().parents[1]
    channels = []
    for channel in ["letter", "web"]:
        frame = pd.read_csv(
            activity_dir / "data" / f"historical_requests_{channel}.csv.gz"
        ).drop_duplicates()
        frame["channel"] = channel
        channels.append(frame)
    data = pd.concat(channels, ignore_index=True)
    data["in_date"] = pd.to_datetime(data["in_date"])
    data["out_date"] = pd.to_datetime(data["out_date"])
    data["answered"] = data["out_date"].notna()
    data["pending"] = ~data["answered"]
    data["year"] = data["in_date"].dt.year
    data["calendar_days"] = (data["out_date"] - data["in_date"]).dt.days
    data["business_days"] = np.nan

    # Contamos desde el dia posterior a la entrada hasta la respuesta incluida.
    answered = data["answered"]
    starts = data.loc[answered, "in_date"].to_numpy(dtype="datetime64[D]")
    ends = data.loc[answered, "out_date"].to_numpy(dtype="datetime64[D]")
    one_day = np.timedelta64(1, "D")
    data.loc[answered, "business_days"] = np.busday_count(
        starts + one_day, ends + one_day
    )
    data["on_time"] = answered & data["business_days"].le(15)

    channel_summary = data.groupby("channel").agg(
        requests=("channel", "size"),
        answered=("answered", "sum"),
        pending=("pending", "sum"),
        median_business_days=("business_days", "median"),
        on_time_rate=("on_time", "mean"),
    ).reset_index()
    yearly_summary = data.groupby(["year", "channel"]).agg(
        requests=("channel", "size"),
        pending=("pending", "sum"),
        on_time_rate=("on_time", "mean"),
    ).reset_index()
    day_order = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    entry_day_summary = data.groupby("day_name").agg(
        requests=("channel", "size"),
        median_calendar_days=("calendar_days", "median"),
        median_business_days=("business_days", "median"),
    ).reindex(day_order).reset_index()

    submission_dir = activity_dir / "submission"
    submission_dir.mkdir(parents=True, exist_ok=True)
    for name, table in [
        ("channel_summary.csv", channel_summary),
        ("yearly_summary.csv", yearly_summary),
        ("entry_day_summary.csv", entry_day_summary),
    ]:
        table.to_csv(submission_dir / name, index=False)
    return channel_summary, yearly_summary, entry_day_summary


if __name__ == "__main__":
    pregunta_01()
