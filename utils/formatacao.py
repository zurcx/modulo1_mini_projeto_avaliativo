import pandas as pd


def padronizar_nome(nome: str) -> str:
    """
    Padroniza um nome removendo espaços extras no início e no fim
    e aplicando capitalização em cada palavra.

    Args:
    nome (str): Nome a ser padronizado.

    Returns:
    str: Nome padronizado.

    Example:
    >>> padronizar_nome("  joÃO silVA  ")
    'João Silva'
    """
    if pd.isna(nome):
        return nome
    return str(nome).strip().title()


def padronizar_categoria(categoria: str) -> str:
    """
    Padroniza uma categoria removendo espaços excedentes
    e aplicando capitalização em cada palavra.

    Args:
        categoria (str): Categoria a ser padronizada.

    Returns:
        str: Categoria padronizada.

    Example:
        >>> padronizar_categoria("  eleTRÔnicos   ")
        'Eletrônicos'
    """
    return " ".join(categoria.split()).lower()
