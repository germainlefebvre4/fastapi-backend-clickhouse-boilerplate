import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401




class Item(Base):
    id = Column(types.UUID(), primary_key=True, index=True, nullable=True)
    title = Column(types.String(), index=True)
    description = Column(types.String(), index=True)
    owner_id = Column(types.UUID(), ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")

    __table_args__ = (
        engines.ReplacingMergeTree(),
        {}
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
