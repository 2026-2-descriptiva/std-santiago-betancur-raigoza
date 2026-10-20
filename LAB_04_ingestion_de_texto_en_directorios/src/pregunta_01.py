# def pregunta_01():
#     """
#     Las frases de este laboratorio no están en una tabla, sino en miles de
#     archivos de texto organizados en carpetas. Dentro de `data/` hay dos
#     carpetas, `train/` y `test/`, y cada una contiene las carpetas
#     `negative/`, `neutral/` y `positive/`. Cada archivo `.txt` contiene una
#     frase, y la carpeta donde se encuentra indica su sentimiento.

#     Su tarea es construir un dataset para cada división y guardarlo en:

#     - `submission/train_dataset.csv`
#     - `submission/test_dataset.csv`

#     Cada archivo debe tener dos columnas: `phrase`, con el texto de la frase,
#     y `target`, con el nombre de la carpeta de sentimiento (`negative`,
#     `neutral` o `positive`). Recorra las carpetas y los archivos en orden
#     alfabético, de modo que el resultado sea siempre el mismo. No guarde el
#     índice de Pandas en el CSV.

#     Ejemplo del formato de cada archivo:

#         phrase,target
#         "The real estate company posted a net loss ...",negative
#         ...
#         "Cardona slowed her vehicle , turned around ...",neutral
#         ...
#     """

#     raise NotImplementedError
from pathlib import Path

import pandas as pd


def pregunta_01():

    root = Path(__file__).resolve().parents[1]
    data_dir = root / "data"
    submission_dir = root / "submission"
    submission_dir.mkdir(exist_ok=True)

    datasets = {}
    for split in ("train", "test"):
        records = []
        for target_dir in sorted((data_dir / split).iterdir()):
            for text_file in sorted(target_dir.glob("*.txt")):
                records.append(
                    {
                        "phrase": text_file.read_text(encoding="utf-8").strip(),
                        "target": target_dir.name,
                    }
                )
        dataset = pd.DataFrame(records, columns=["phrase", "target"])
        dataset.to_csv(submission_dir / f"{split}_dataset.csv", index=False)
        datasets[split] = dataset

    return datasets["train"], datasets["test"]
    # raise NotImplementedError
