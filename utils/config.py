# configuração do Path (caminho para acesso aos arquivos)

from pathlib import Path

Path("outputs").mkdir(exist_ok=True)
BASE_DIR = Path(__file__).resolve().parent.parent


# configuração dos diretorios
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"

OUTPUT_DIR.mkdir(exist_ok=True)
