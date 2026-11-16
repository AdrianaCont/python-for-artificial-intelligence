#Revisar campos obligatorios, nulos, duplicados y producir un resumen básico.
import pandas as pd


def validate_dataset(df, required_columns):
    """
    Realiza validaciones básicas de calidad sobre un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset a validar.

    required_columns : list
        Columnas consideradas obligatorias.

    Returns
    -------
    pandas.DataFrame
        Resumen de calidad del dataset.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Columnas faltantes: {missing_columns}"
        )

    null_values = (
        df[required_columns]
        .isna()
        .sum()
        .sum()
    )

    duplicated_rows = (
        df.duplicated()
        .sum()
    )

    quality_summary = pd.DataFrame({
        "Metric": [
            "Rows",
            "Columns",
            "Missing values in required fields",
            "Duplicated rows"
        ],
        "Value": [
            df.shape[0],
            df.shape[1],
            null_values,
            duplicated_rows
        ]
    })

    return quality_summary