# Modele ORM – przykładowa tabela Users
from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)

    def to_dict(self) -> dict:
        # Pomocnicza metoda do serializacji obiektu do JSON
        return {"id": self.id, "name": self.name, "email": self.email}
