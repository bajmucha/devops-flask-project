"""
Jednorazowy skrypt migracji uruchamiany w kontenerze migration_runner.

Tworzy tabele w bazie danych na podstawie modeli SQLAlchemy.
"""

import os
import sys

# Dodajemy katalog nadrzędny (/app) do sys.path,
# żeby można było importować moduł "src"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)  # /app
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.db import engine
from src.models import Base


def run_migrations() -> None:
    # Tworzymy wszystkie tabele, jeśli jeszcze nie istnieją
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    run_migrations()
