import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Identity
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from clickhouse_sqlalchemy import (
    Table, make_session, get_declarative_base, types, engines
)

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401




class User(Base):
    id = Column(types.UUID(), primary_key=True, nullable=False)
    full_name = Column(types.String(), index=True)
    email = Column(types.String(), unique=True, index=True, nullable=False)
    hashed_password = Column(types.String(), nullable=False)
    is_active = Column(types.Boolean(), default=True)
    is_superuser = Column(types.Boolean(), default=False)
    items = relationship("Item", back_populates="owner")

    __table_args__ = (
        engines.MergeTree(primary_key=('id'), order_by=('email')),
        {}
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())
