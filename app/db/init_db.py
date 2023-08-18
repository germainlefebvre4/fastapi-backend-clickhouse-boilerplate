from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.db import base  # noqa: F401

from dotenv import load_dotenv
load_dotenv()

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)

    print("Create user admin")
    user_admin = crud.user.get_by_email(db, email=settings.USER_ADMIN_EMAIL)
    if not user_admin:
        user_in = schemas.UserCreate(
            email=settings.USER_ADMIN_EMAIL,
            full_name=settings.USER_ADMIN_FULLNAME,
            password=settings.USER_ADMIN_PASSWORD,
            is_superuser=True,
        )
        user_admin = crud.user.create(db, obj_in=user_in)  # noqa: F841

    print("Create user test")
    user_test = crud.user.get_by_email(db, email=settings.USER_TEST_EMAIL)
    if not user_test:
        user_in = schemas.UserCreate(
            email=settings.USER_TEST_EMAIL,
            full_name=settings.USER_TEST_FULLNAME,
            password=settings.USER_TEST_PASSWORD,
            is_superuser=False,
        )
        user_test = crud.user.create(db, obj_in=user_in)  # noqa: F841
