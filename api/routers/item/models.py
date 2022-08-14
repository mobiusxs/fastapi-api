from sqlalchemy import Column
from sqlalchemy import String

from api.database import Base


class Item(Base):
    name = Column(String(120), unique=False, nullable=True)
