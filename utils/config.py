# configuração do Path (caminho para acesso aos arquivos)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# configuração dos diretorios
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
