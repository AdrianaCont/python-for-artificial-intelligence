import pandas as pd


def analyze_products(df):
    """
    Resume ventas por número de parte.

    Returns
    -------
    pandas.DataFrame
        Cantidad e importe vendido por producto.
    """

    analysis_df = df.copy()

    analysis_df["im_ImporteVenta"] = (
        analysis_df["ct_Cantidad"]
        * analysis_df["im_PrecioVenta"]
    )

    product_analysis = (
        analysis_df
        .groupby(
            "cd_NumParte",
            as_index=False
        )
        .agg(
            cantidad_vendida=(
                "ct_Cantidad",
                "sum"
            ),
            importe_vendido=(
                "im_ImporteVenta",
                "sum"
            )
        )
        .sort_values(
            "cantidad_vendida",
            ascending=False
        )
    )

    return product_analysis


def analyze_customers(df):
    """
    Resume el comportamiento comercial por cliente.

    Returns
    -------
    pandas.DataFrame
        Cantidad, importe y variedad de productos
        comprados por cliente.
    """

    analysis_df = df.copy()

    analysis_df["im_ImporteVenta"] = (
        analysis_df["ct_Cantidad"]
        * analysis_df["im_PrecioVenta"]
    )

    customer_analysis = (
        analysis_df
        .groupby(
            "cd_IdClienteFC",
            as_index=False
        )
        .agg(
            cantidad_comprada=(
                "ct_Cantidad",
                "sum"
            ),
            importe_comprado=(
                "im_ImporteVenta",
                "sum"
            ),
            productos_distintos=(
                "cd_NumParte",
                "nunique"
            )
        )
        .sort_values(
            "importe_comprado",
            ascending=False
        )
    )

    return customer_analysis