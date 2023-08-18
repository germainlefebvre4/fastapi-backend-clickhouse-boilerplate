# from typing import Any

# from sqlalchemy.ext.declarative import as_declarative, declared_attr


# @as_declarative()
# class Base:
#     id: Any
#     __name__: str
#     # Generate __tablename__ automatically
#     @declared_attr
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()

from clickhouse_sqlalchemy import get_declarative_base
from app.db.session import metadata

Base = get_declarative_base(metadata=metadata)
