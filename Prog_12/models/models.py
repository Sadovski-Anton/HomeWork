from datetime import datetime
from sqlalchemy import (Column, SmallInteger, VARCHAR, ForeignKey,
                        TIMESTAMP, CHAR, DECIMAL, Boolean)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    parent_id = Column(
        SmallInteger, ForeignKey('categories.id', ondelete='CASCADE')
    )


class Product(Base):
    __tablename__: str = 'products'

    article = Column(CHAR(6), primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    descr = Column(VARCHAR(140))
    category_id = Column(
        SmallInteger,
        ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False
    )


class User(Base):
    __tablename__: str = 'users'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False)
    email = Column(VARCHAR(20), nullable=False, unique=True)


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(SmallInteger, primary_key=True)
    user_id = Column(
        SmallInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    is_pad = Column(Boolean, default=False, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False)


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(SmallInteger, primary_key=True)
    product_article = Column(
        CHAR(6), ForeignKey('products.article', ondelete='NO ACTION'), nullable=False
    )
    order_id = Column(
        SmallInteger, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False
    )
