from app.core.config import settings

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from clickhouse_sqlalchemy import (
    make_session, get_declarative_base
)

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
metadata = MetaData(bind=engine)
SessionLocal = make_session(engine)
