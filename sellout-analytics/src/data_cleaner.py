import pandas as pd


def clean_sales_data(df):
    """
    Estandariza y aplica reglas básicas de calidad
    al dataset de ventas.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset de ventas.

    Returns
    -------
    pandas.DataFrame
        Dataset limpio con banderas de calidad.
    """

    clean_df = df.copy()

    # Normalizar número de parte
    clean_df["cd_NumParte"] = (
        clean_df["cd_NumParte"]
        .astype("string")
        .str.strip()
        .str.upper()
    )

    # Convertir fecha
    clean_df["fh_Fecha"] = pd.to_datetime(
        clean_df["fh_Fecha"],
        errors="coerce",
        dayfirst=True
    )

    # Reglas de calidad
    clean_df["fl_ParteValida"] = (
        clean_df["cd_NumParte"].notna()
        &
        (clean_df["cd_NumParte"] != "")
    )

    clean_df["fl_CantidadValida"] = (
        clean_df["ct_Cantidad"].notna()
        &
        (clean_df["ct_Cantidad"] > 0)
    )

    clean_df["fl_PrecioValido"] = (
        clean_df["im_PrecioVenta"].notna()
        &
        (clean_df["im_PrecioVenta"] > 0)
    )

    clean_df["fl_FechaValida"] = (
        clean_df["fh_Fecha"].notna()
    )

    clean_df["fl_RegistroValido"] = (
        clean_df["fl_ParteValida"]
        &
        clean_df["fl_CantidadValida"]
        &
        clean_df["fl_PrecioValido"]
        &
        clean_df["fl_FechaValida"]
    )

    return clean_df