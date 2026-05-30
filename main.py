# Importando modulos

print("\n" + " Importando modulos... ".center(80, "=") + "\n")
import pandas as pd
import time
# Meus modulos

from utils.config import DATA_DIR
from utils import Evidencias
from utils.formatacao import padronizar_nome
from utils.limpeza import tratar_falso_nulos

print(" Modulos carregados com sucesso!".center(80, "="))

# Configuração Path para acesso aos arquivos

arquivo_base = DATA_DIR / "base_varejo.csv"
arquivo = "base_varejo.csv"


# Ignorando warning message


# Carregar o dataset

print("\n" + " Carregando Arquivo base Varejo para Análise ".center(80, "=") + "\n")
print()

df = pd.read_csv(arquivo_base, sep=";")

print("Carregando", end="")
for _ in range(5):
    time.sleep(0.5)
    print(".", end="", flush=True)
print(f"\nCarregamento do arquivo {arquivo} foi concluído!" + "\n")

# Exibição das 10 primeira linhas
print("\n" + " As 10 primeiras linhas do DataSet".center(80, "=") + "\n")
print(df.head(10))

# Exibição das 10 ultimas linhas
print("\n\n" + " As 10 ultimas linhas do DataSet".center(80, "=") + "\n")
print(df.tail(10))

#  Mostrar o tamanho (linhas e colunas)

print("\n" + " Tamanho do Dataset ".center(80, "=") + "\n")

tamanho = (
    f"Quantidade de linhas:  {df.shape[0]}  | Quantidade de colunas: {df.shape[1]}"
)
print(f"{tamanho.center(80)}\n")
print("\n" + " Fim bloco Tamanho Dataset ".center(80, "=") + "\n")

print("\n" + " Tipos de dado das colunas ".center(80, "=") + "\n")

print(df.dtypes)
print("\n" + " Fim bloco Tipos de dados ".center(80, "=") + "\n")
print(" Colunas do Dataset:".center(80, "="))
print()
print(df.columns)
print()
print("\n" + " Fim bloco Colunas ".center(80, "="))
print()

Evidencias(df, "Base de Loja Varejo")

print("\n" + " TRATAMENTO DOS DADOS ".center(80, "=") + "\n")

# Remoção das colunas unnamed

df = df.dropna(axis=1, how="all")

print(df.columns)


# Padronização de produto

df["PR_NOME"] = df["PR_NOME"].apply(padronizar_nome)

# Padronização de categoria
#
df["PR_CAT"] = df["PR_CAT"].apply(padronizar_nome)

print("\n" + f"Validação padronização coluna PR_NOME:\n \n{df['PR_NOME']}")
print("\n" + f"Validação padronização coluna PR_CAT:\n \n{df['PR_CAT']}")

# Tratar falso nulos

df = tratar_falso_nulos(df)
df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")
Evidencias(df, "Base de Loja Varejo")
