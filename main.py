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
print()
"""
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
"""
Evidencias(df, "Base de Loja Varejo")

print("\n" + " TRATAMENTO DOS DADOS ".center(80, "=") + "\n")

# Remoção das colunas unnamed

df = df.dropna(axis=1, how="all")

# print(df.columns)


# Padronização de produto

df["PR_NOME"] = df["PR_NOME"].apply(padronizar_nome)

# Padronização de categoria
#
df["PR_CAT"] = df["PR_CAT"].apply(padronizar_nome)

print("\n" + f"Validação padronização coluna PR_NOME:\n \n{df['PR_NOME']}")
print("\n" + f"Validação padronização coluna PR_CAT:\n \n{df['PR_CAT']}")

# Tratar falso nulos

df = tratar_falso_nulos(df)
df.loc[df["PR_CAT"] == "#N/D", "PR_CAT"] = "Outros"

# Tratar tipos de dados

df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")

qtd_nulos_datas = df["DATA"].isna().sum()
perc_nulos = qtd_nulos_datas / len(df) * 100

print(f"percentual de datas nulas: {perc_nulos:.2f}%")

# Devido ao percentual de nulos vamos separar

print("\n" + " Dados df com datas preenchidas".center(80, "=") + "\n")
df_com_data = df[df["DATA"].notna()]
print(f"Linhas:     {df_com_data.shape[0]}")
print(f"Colunas:    {df_com_data.shape[1]}")
print()
print(df_com_data.head(10))

print("\n" + " Dados df sem datas preenchidas".center(80, "=") + "\n")
df_sem_data = df[df["DATA"].isna()]
print(f"Linhas:     {df_sem_data.shape[0]}")
print(f"Colunas:    {df_sem_data.shape[1]}")
print()
print(df_sem_data.head(10))

"""
# cliente 814

df_814 = df[df["CL_ID"] == 814]

print("cliente 814")
print(df_814.head())
print(df_814.shape)
df.groupby("CO_ID")["DATA"].nunique().sort_values(ascending=False).head(10)
df[df["DATA"].isna()]["CL_ID"].value_counts().head(10)
df[df["DATA"].isna()]["CL_ID"].value_counts().head(10)
print(df[df["CO_ID"] == 8878]["DATA"])
"""

qtd_duplicados_data = df.duplicated(subset=["DATA", "CL_ID", "PR_NOME"]).sum()

# tratar qtd_duplicados

print("\n" + " Quantidade de registros duplicados ".center(80, "=") + "\n")

duplicados = df[df.duplicated(subset=["DATA", "CO_ID", "CL_ID"], keep=False)]

print(duplicados.head())

print("\n" + " Amostra de duplicados ".center(80, "=") + "\n")
print(duplicados["CO_ID"].value_counts())
print()
print(duplicados.head(10))

# tratar Duplicatas

df_limpo = df.drop_duplicates(subset=["DATA", "CO_ID", "CL_ID"], keep="first")

Evidencias(df_limpo, "Base de Loja Varejo")


# estatistica numero de filhos

print("\n" + " Estatística sobre filhos dos clientes".center(80, "=") + "\n")

estat_filhos = df_limpo["CL_FHL"].describe().round(2)
print(estat_filhos)


# Agrupamento da analise


print("\n" + " Agrupamento por categoria ".center(80, "=") + "\n")
resumo_categ = (
    df_limpo.groupby("PR_CAT")
    .agg(
        total=("PR_ID", "sum"),
        media=("PR_ID", "mean"),
        quantidade=("PR_ID", "count"),
        maximo=("PR_ID", "max"),
    )
    .sort_values("total", ascending=False)
)

print(resumo_categ)

print("\n" + " Agrupamento por categoria ".center(80, "=") + "\n")
resumo_filhos_categ = (
    df_limpo.groupby("PR_CAT")
    .agg(media_filhos=("CL_FHL", "mean"), clientes=("CL_ID", "nunique"))
    .round(2)
)

print(resumo_filhos_categ)


print("\n" + " Resumo da análise".center(80, "=") + "\n")
print("* Presença de espaços em branco no início e/ou final dos valores da coluna")
print("* Existência de colunas não nomeadas (Unnamed), sem relevância para a análise.")
print(
    "* Identificação da categoria '#N/D', indicando ausência ou inconsistência na classificação do produto."
)
print(
    "* Remoção das colunas não nomeadas (Unnamed), por não agregarem valor ao processo analítico."
)
print(
    "* Conversão das colunas de data para o tipo adequado (datetime), permitindo análises temporais mais precisas."
)
