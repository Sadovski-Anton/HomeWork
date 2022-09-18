from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Prog_12.models import Category, Product, create_sync_session


class CRUDProduct:

    @staticmethod
    @create_sync_session
    def add(
        article: str,
        name: str = None,
        price: int = None,
        descr: str = None,
        category_id: int = None,
        session: Session = None)\
            -> Optional[Product]:
        product = Product(
            article=article,
            name=name,
            price=price,
            descr=descr,
            category_id=category_id
        )
        session.add(product)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(product)
            return product

    @staticmethod
    @create_sync_session
    def get(product_id: int, session: Session = None) -> Optional[Product]:
        product = session.execute(
            select(Category).where(Category.id == product_id)
        )
        product = product.first()
        if product:
            return product[0]

    @staticmethod
    @create_sync_session
    def all(category_id: int = None, session: Session = None) -> List[Product]:
        if category_id:
            products = session.execute(
                select(Product).where(Product.category_id == category_id)
                .order_by(Product.id)
            )
        else:
            products = session.execute(
                select(Product)
                .order_by(Product.id)
            )
        return [product[0] for product in products]

    @staticmethod
    @create_sync_session
    def delete(product_id: int, session: Session = None) -> None:
        session.execute(
            delete(Product)
            .where(Product.id == product_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(
            product_id: int,
            article: str = None,
            name: str = None,
            price: int = None,
            date_created: str = None,
            descr: str = None,
            category_id: int = None,
            session: Session = None
    ) -> bool:
        if name or article or price or date_created or descr or category_id:
            session.execute(
                update(Product)
                .where(Product.id == product_id)
                .values(
                    article=article if article else Product.article,
                    name=name if name else Product.name,
                    price=price if price else Product.price,
                    date_created=date_created if date_created else Product.date_created,
                    category_id=category_id if category_id else Product.category_id,
                )
            )
            try:
                session.commit()
            except IntegrityError:
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    @create_sync_session
    def join(product_id: int = None, session: Session = None) -> List[Tuple[Product, Category]]:
        if product_id:
            response = session.execute(
                select(Product, Category)
                .join(Category, Product.id == Category.product_id)
                .where(Product.id == product_id)
            )
        else:
            response = session.execute(
                select(Category, Product)
                .join(Category, Product.id == Category.product_id)
                )
        return response.all()
