from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Prog_12.models import OrderItem, Product, Order, create_sync_session


class CRUDOrderItem:

    @staticmethod
    @create_sync_session
    def add(product_article: str, order_id: int = None, session: Session = None) -> Optional[OrderItem]:
        order_item = OrderItem(
            product_article=product_article,
            order_id=order_id
        )
        session.add(order_item)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(order_item)
            return order_item

    @staticmethod
    @create_sync_session
    def get(order_item_id: int, session: Session = None) -> Optional[OrderItem]:
        order_item = session.execute(
            select(OrderItem).where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return order_item[0]

    @staticmethod
    @create_sync_session
    def all(order_id: int = None, session: Session = None) -> List[OrderItem]:
        if order_id:
            order_items = session.execute(
                select(OrderItem).where(OrderItem.order_id == order_id)
                .order_by(OrderItem.id)
            )
        else:
            order_items = session.execute(
                select(OrderItem)
                .order_by(OrderItem.id)
            )
        return [order_id[0] for order_id in order_items]

    @staticmethod
    @create_sync_session
    def delete(order_item_id: int, session: Session = None) -> None:
        session.execute(
            delete(OrderItem)
            .where(OrderItem.id == order_item_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(
            order_item_id: int,
            order_id: int = None,
            product_article: str = None,
            session: Session = None
    ) -> bool:
        if product_article or order_id:
            session.execute(
                update(OrderItem)
                .where(OrderItem.id == order_item_id)
                .values(
                    order_id=order_id if order_id else OrderItem.order_id,
                    product_article=product_article if product_article else OrderItem.product_article
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
    def join(order_item_id: int = None, session: Session = None) -> List[Tuple[OrderItem, Product, Order]]:
        if order_item_id:
            response = session.execute(
                select(OrderItem, Product, Order)
                .join(Order, Product, OrderItem.id == Product.order_item_id, OrderItem.id == Order.order_item_id)
                .where(OrderItem.id == order_item_id)
            )
        else:
            response = session.execute(
                select(OrderItem, Product, Order)
                .join(Order, Product, OrderItem.id == Product.order_item_id, OrderItem.id == Order.order_item_id)
                )
        return response.all()
