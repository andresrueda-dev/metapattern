import pandas as pd
import os
from datetime import datetime

def guardar(data_file, combinaciones):
    df = pd.DataFrame({
        "fecha": [datetime.now()] * len(combinaciones),
        "numeros": [",".join(map(str, c)) for c in combinaciones],
        "resultado": ["" for _ in combinaciones],
        "aciertos": [0 for _ in combinaciones]
    })

    if os.path.exists(data_file):
        df.to_csv(data_file, mode='a', header=False, index=False)
    else:
        df.to_csv(data_file, index=False)


def cargar(data_file):
    if os.path.exists(data_file):
        return pd.read_csv(data_file)
    return pd.DataFrame(columns=["fecha", "numeros", "resultado", "aciertos"])
