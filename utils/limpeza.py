import numpy as np

"""
Função trata falso nulos
ex.:
    'NULL'
    'N/A'
    'NA'
    'NAN'
    '-'
    ' '
"""


def tratar_falso_nulos(df) -> None:
    falso_nulos = ["NULL", "N/A", "NA", "NAN", "-", " "]
    return df.replace(falso_nulos, np.nan)
