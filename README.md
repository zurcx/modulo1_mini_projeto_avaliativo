
# Problemas encontrados
## Espaços no inicio da Categoria (PR_CAT)
## Espaços no inicio da Nome do Produto (PR_NOME)
## Colunas nao nomeadas
## Colunas com valores nulos


# Etapas de limpeza
## Removida colunas unnamed e com dados nulos
## Conversão do tipo relacionada a data.
## Identificado datas nulas, porém a opção foi a verificação em outras fontes que possam dar mais evidencia para tomada de decisão
## Encontrado uma categoria '#N/D' foi classificada com 'Outros'

# Mini Projeto Avaliativo - Análise de Dados

Projeto desenvolvido como parte da trilha de Análise de Dados utilizando Python e Pandas.

## Estrutura do Projeto

```text
.
├── data/
│   └── base_varejo.csv
├── notebooks/
│   └── main.ipynb
├── outputs/
├── utils/
│   ├── __init__.py
│   ├── evidencias.py
│   └── formatacao.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Pré-requisitos

* Python 3.12+
* Git

## Instalação

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd modulo1_mini_projeto_avaliativo
```

### 2. Criar o ambiente virtual

Linux/macOS:

```bash
python3 -m venv venv
```

Windows:

```powershell
python -m venv venv
```

### 3. Ativar o ambiente virtual

Linux/macOS:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

## Execução

Executar o script principal:

```bash
python main.py
```

## Notebook

Para abrir o notebook:

```bash
jupyter notebook
```

Em seguida, acesse:

```text
notebooks/main.ipynb
```

## Bibliotecas Utilizadas

* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook






# Problemas Identificados

Durante a etapa de análise exploratória dos dados (EDA), foram identificadas as seguintes inconsistências:

* Presença de espaços em branco no início e/ou final dos valores da coluna **PR_CAT** (Categoria do Produto).
* Presença de espaços em branco no início e/ou final dos valores da coluna **PR_NOME** (Nome do Produto).
* Existência de colunas não nomeadas (*Unnamed*), sem relevância para a análise.
* Presença de valores nulos em algumas colunas do conjunto de dados.
* Identificação da categoria **"#N/D"**, indicando ausência ou inconsistência na classificação do produto.
* Registros com datas ausentes em colunas relacionadas ao processo de vendas.

# Etapas de Limpeza e Tratamento dos Dados

Para garantir a qualidade e consistência das análises, foram realizadas as seguintes ações:

1. Remoção das colunas não nomeadas (*Unnamed*), por não agregarem valor ao processo analítico.
2. Tratamento dos valores nulos e remoção de colunas sem relevância para a análise.
3. Padronização dos campos textuais, removendo espaços excedentes e ajustando a formatação dos valores.
4. Conversão das colunas de data para o tipo adequado (`datetime`), permitindo análises temporais mais precisas.
5. Identificação de registros com datas ausentes. Optou-se por não realizar imputação automática, recomendando validação em fontes complementares para maior confiabilidade na tomada de decisão.
6. Reclassificação da categoria **"#N/D"** para **"Outros"**, permitindo sua inclusão nas análises sem comprometer a segmentação dos dados.

# Considerações

As etapas de tratamento foram realizadas com o objetivo de melhorar a qualidade dos dados e reduzir possíveis impactos de inconsistências nas análises estatísticas e na geração de indicadores.

## Autor

Luiz Fabio da Cruz


