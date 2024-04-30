from datetime import datetime
from typing import Optional
from sqlalchemy.sql.functions import func
from sqlalchemy import URL, create_engine, BIGINT, VARCHAR, ForeignKey, String, INTEGER
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from typing_extensions import Annotated
from sqlalchemy.ext.declarative import declared_attr

url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="testpassword",
    host="localhost",
    database="testuser",
    port=5432
)

engine = create_engine(url, echo=True)
session_pool = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


# class User(Base):
#     __tablename__ = "users"
#
#     telegram_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
#     full_name: Mapped[str] = mapped_column(VARCHAR(255))
#     username: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
#     language_code: Mapped[str] = mapped_column(VARCHAR(255))
#     created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
#     referrer_id: Mapped[Optional[int]] = mapped_column(BIGINT,
#                                                        ForeignKey("users.telegram_id",
#                                                                   ondelete="SET NULL"))


class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())


class Users(Base, TimeStampMixin):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    username: Mapped[Optional[str]] = mapped_column(VARCHAR(255), nullable=True)
    language_code: Mapped[str] = mapped_column(VARCHAR(255))
    referrer_id: Mapped[Optional[int]] = mapped_column(BIGINT,
                                                       ForeignKey("users.telegram_id",
                                                                  ondelete="SET NULL"))


user_fk = Annotated[int, mapped_column(BIGINT, ForeignKey("users.telegram_id", ondelete="CASCADE"))]

int_pk = Annotated[int, mapped_column(INTEGER, primary_key=True)]

str_255 = Annotated[str, mapped_column(String(255))]


class TableNameMixin:
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Orders(Base, TimeStampMixin, TableNameMixin):
    order_id: Mapped[int_pk]
    user_id: Mapped[user_fk]


class Products(Base, TimeStampMixin, TableNameMixin):
    product_id: Mapped[int_pk]
    title: Mapped[str_255]
    description: Mapped[str]


class OrderProducts(Base, TableNameMixin):
    order_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("orders.order_id", ondelete="CASCADE"), primary_key=True)
    product_id: Mapped[int] = mapped_column(INTEGER, ForeignKey("products.product_id", ondelete="RESTRICT"),
                                            primary_key=True)
    quantity: Mapped[int]


Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)



























