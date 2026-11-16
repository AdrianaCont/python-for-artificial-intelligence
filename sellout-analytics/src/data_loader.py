#Cargar un CSV y presetnar los identificadores como texto
import pandas as pd
from pathlib import Path

def load_dataset(file_path, dtype=None):
    """
    Carga un archivo CSV y devuelve un DataFrame.

    Parameters
    ----------
    file_path : str or Path
        Ruta del archivo CSV.

    dtype : dict, optional
        Tipos de datos que deben conservarse
        durante la lectura.

    Returns
    -------
    pandas.DataFrame
        Dataset cargado.
    """

    try:

        df = pd.read_csv(
            file_path,
            dtype=dtype
        )

        print(
            f"Dataset cargado correctamente: "
            f"{df.shape[0]} filas, "
            f"{df.shape[1]} columnas."
        )

        return df

    except FileNotFoundError:
        print(
            f"Error: archivo no encontrado: "
            f"{file_path}"
        )

        return None