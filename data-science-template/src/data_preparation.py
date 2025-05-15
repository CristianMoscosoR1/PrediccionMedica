import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Carga un archivo CSV y lo devuelve como un DataFrame de pandas."""
    return pd.read_csv(path)