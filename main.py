# Importando modulos

print(" Importando modulos... ".center(80, "="))
import pandas as pd

# Meus modulos

from utils.config import DATA_DIR

print(" Modulos carregados com sucesso!".center(80, "="))

# Configuração Path para acesso aos arquivos

arquivo_base = DATA_DIR / "base_varejo.csv"


# Ignorando warning message


# Carregar o dataset

print("\n" + " Carregando Arquivo base Varejo para Análise ".center(80, "="))
print()
df = pd.read_csv(arquivo_base, sep=";")

print()
print(df.head(10))
print()

#  Mostrar o tamanho (linhas e colunas)

print(" Tamanho do Dataset: ".center(80, "="))

tamanho = f"Quantidade de linhas:  {df.shape[0]} | Quantidade de colunas: {df.shape[1]}"

print(f"\n{tamanho.center(80)}\n")

print(" Fim bloco Tamanho Dataset ".center(80, "="))
print()
print(" Tipos de dado das colunas ".center(80, "="))
print()
print(df.dtypes)
print("\n" + " Fim bloco Tipos de dados".center(80, "="))


def evidencias(df, nome="DataFrame"):
    """
    Dispõe um relatório completo de consistência dos dados.
    """

    print("=" * 80)
    print(" EVIDÊNCIAS - {nome}".center(80))
    print("=" * 80)
    print(f" Linhas:            {df.shape[0]}")
    print(f" Colunas:           {df.shape[1]}")
    print(f" Linhas duplicadas: {df.duplicated().sum()}")
    print()

    nulos = df.isnull().sum()
    pct = (nulos / len(df) * 100).round(1)

    print(" Coluna          | Tipo               | Nulos | % Nulos")
    print("  " + "-" * 50)
    for col in df.columns:
        tipo = str(df[col].dtypes)
        print(f" {col:<18} |  {tipo:<10} |  {nulos[col]:<5} |  {pct[col]}%")
    print("=" * 80)
