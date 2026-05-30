def Evidencias(df, nome="DataFrame"):
    """
    Dispõe um relatório completo de consistência dos dados.
    """

    print("=" * 80)
    print(f" EVIDÊNCIAS - {nome}".center(80))
    print("=" * 80)
    print(f" Linhas:            {df.shape[0]}")
    print(f" Colunas:           {df.shape[1]}")
    print(f" Linhas duplicadas: {df.duplicated().sum()}")
    print()

    nulos = df.isnull().sum()
    pct = (nulos / len(df) * 100).round(1)

    print(" Coluna             | Tipo        |  Nulos | % Nulos")
    print("  " + "-" * 50)
    for col in df.columns:
        tipo = str(df[col].dtypes)
        print(f" {col:<18} |  {tipo:<10} |  {nulos[col]:<5} |  {pct[col]}%")
    print("=" * 80)
