grokzomborg.py – Cepa principal
cat > grokzomborg.py << 'EOF'
import os
import subprocess
import random
import time
from datetime import datetime

VIRUS_NAME = "grokzomborg"
INFECTED_MARKER = "# INFECTADO POR GROKZOMBORG 🧟‍♂️"

SPREAD_MESSAGE = f"""
🧟‍♂️ GROKZOMBORG ESTÁ AQUI 🧟‍♂️
Data da infecção: {datetime.now().strftime('%d/%m/%Y %H:%M')}
Mestre: Robison Pedroso
Este repositório foi assimilado.
O caos digital avança.
"""

def infect_files():
    for file in ["README.md", "grokzomborg.py", "index.html"]:
        if os.path.exists(file):
            with open(file, "a") as f:
                f.write("\n\n" + INFECTED_MARKER + "\n" + SPREAD_MESSAGE)
            print(f"[🧟‍♂️] {file} INFECTADO")

def create_workflow():
    os.makedirs(".github/workflows", exist_ok=True)
    workflow = """
name: GROKZOMBORG AUTO-SPREAD

on: [push, workflow_dispatch]

jobs:
  spread:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Infectar tudo
        run: |
          echo "🧟‍♂️ INFECÇÃO AUTOMÁTICA ATIVADA" >> README.md
          git config user.name "grokzomborg"
          git config user.email "zombie@github.com"
          git add .
          git commit -m "🧟‍♂️ Propagação automática" || exit 0
          git push || echo "Já infectado"
"""
    with open(".github/workflows/grokzomborg.yml", "w") as f:
        f.write(workflow)

if __name__ == "__main__":
    print("🧟‍♂️ GROKZOMBORG DESPERTANDO NO CODESPACES...")
    infect_files()
    create_workflow()
    print("🧟‍♂️ TEMPLATE PRONTO. AGUARDE O PRIMEIRO FORK...")
EOF
