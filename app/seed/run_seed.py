"""
Seeder uruchamiany jako osobny kontener (seed_runner).

Zadania:
- połączyć się z bazą PostgreSQL,
- wypełnić ją przykładowymi danymi,
- wygenerować pliki:
    - seed.log
    - users.csv
    - data.json
  zapisane do wolumenu /seed_output,
- zakończyć działanie (restart: "no").
"""

import csv
import json
import os
import sys
from datetime import datetime

# Dodajemy katalog nadrzędny (/app) do sys.path,
# żeby można było importować moduł "src"
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)  # /app
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.db import SessionLocal
from src.models import User

SEED_OUTPUT_DIR = os.getenv("SEED_OUTPUT_DIR", "/seed_output")


def seed_db() -> None:
    session = SessionLocal()

    users = [
        User(name="Anna Kowalska", email="anna@example.com"),
        User(name="Jan Nowak", email="jan@example.com"),
        User(name="Ola Zielinska", email="ola@example.com"),
        User(name="Piotr Malinowski", email="piotr@example.com"),
        User(name="Kasia Lewandowska", email="kasia@example.com"),
    ]

    # Czyścimy istniejące dane (dla uproszczenia)
    session.query(User).delete()
    for u in users:
        session.add(u)
    session.commit()

    # Pobieramy z bazy, żeby mieć id
    all_users = session.query(User).all()
    session.close()

    os.makedirs(SEED_OUTPUT_DIR, exist_ok=True)

    # Plik CSV
    csv_path = os.path.join(SEED_OUTPUT_DIR, "users.csv")
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "email"])
        for u in all_users:
            writer.writerow([u.id, u.name, u.email])

    # Plik JSON
    json_path = os.path.join(SEED_OUTPUT_DIR, "data.json")
    with open(json_path, mode="w", encoding="utf-8") as f:
        json.dump([u.to_dict() for u in all_users], f, ensure_ascii=False, indent=2)

    # Plik log
    log_path = os.path.join(SEED_OUTPUT_DIR, "seed.log")
    with open(log_path, mode="a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.utcnow().isoformat()}] Zasiane {len(all_users)} rekordów.\n"
        )


if __name__ == "__main__":
    seed_db()
