from datetime import datetime
from sqlalchemy import (Column, SmallInteger, VARCHAR, ForeignKey,
                        TIMESTAMP, CHAR, DECIMAL, Boolean)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(20), nullable=False, unique=True)
    is_published = Column(Boolean, default=False, nullable=False)
    parent_id = Column(
        SmallInteger,
        ForeignKey('categories.id', ondelete='CASCADE')
    )


class Product(Base):
    __tablename__: str = 'products'

    id = Column(
        SmallInteger,
        ForeignKey('categories.id', ondelete='CASCADE'),
        primary_key=True
    )
    category_id = Column(SmallInteger, nullable=False)
    is_published = Column(Boolean, default=False, nullable=False)
    name = Column(VARCHAR(20), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False, default=0)
    media = Column(CHAR(140))
    total = Column(DECIMAL(8, 2), nullable=False)


class Language(Base):
    __tablename__: str = 'languages'

    id = Column(SmallInteger, primary_key=True)
    language_code = Column(VARCHAR(20), nullable=False)


class BotUser(Base):
    __tablename__: str = 'bot_users'

    id = Column(
        SmallInteger,
        ForeignKey('languages.id', ondelete='CASCADE'),
        primary_key=True
    )
    balance = Column(SmallInteger, nullable=False)
    is_blocked = Column(Boolean, default=False, nullable=False)
    language_id = Column(SmallInteger, default=False, nullable=False)


class Status(Base):
    __tablename__: str = 'statuses'

    id = Column(SmallInteger, primary_key=True)
    balance = Column(SmallInteger, nullable=False)
    name = Column(VARCHAR(20), default=False, nullable=False)


class Invoice(Base):
    __tablename__: str = 'invoices'

    id = Column(
        SmallInteger,
        ForeignKey('statuses.id', ondelete='CASCADE'),
        ForeignKey('bot_users.id', ondelete='CASCADE'),
        primary_key=True
    )
    bot_user_id = Column(VARCHAR(20), nullable=False)
    total = Column(SmallInteger, nullable=False, default=False)
    status_id = Column(SmallInteger, default=False, nullable=False)


class Order(Base):
    __tablename__: str = 'orders'

    id = Column(
        SmallInteger,
        ForeignKey('statuses.id', ondelete='CASCADE'),
        ForeignKey('bot_users.id', ondelete='CASCADE'),
        ForeignKey('invoices.id', ondelete='CASCADE'),
        primary_key=True
    )
    bot_user_id = Column(VARCHAR(20), nullable=False)
    total = Column(SmallInteger, nullable=False, default=False)
    status_id = Column(SmallInteger, default=False, nullable=False)
    invoice_id = Column(VARCHAR(20), default=False, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())


class OrderItem(Base):
    __tablename__: str = 'order_items'

    id = Column(
        SmallInteger,
        ForeignKey('products.id', ondelete='CASCADE'),
        ForeignKey('orders.id', ondelete='CASCADE'),
        primary_key=True
    )
    order_id = Column(SmallInteger, nullable=False)
    product_id = Column(SmallInteger, default=False)
    total = Column(SmallInteger, default=0, nullable=False)
