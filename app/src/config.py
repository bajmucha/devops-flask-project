import os

# Konfiguracja aplikacji Flask w jednym miejscu
class Config:
    # Dane do połączenia z bazą – pobierane z zmiennych środowiskowych
    DB_USER = os.getenv("POSTGRES_USER", "app_user")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "app_password")
    DB_NAME = os.getenv("POSTGRES_DB", "app_db")
    DB_HOST = os.getenv("POSTGRES_HOST", "db")
    DB_PORT = os.getenv("POSTGRES_PORT", "5432")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
