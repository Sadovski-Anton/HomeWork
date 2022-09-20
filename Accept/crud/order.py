from typing import Optional, List, Tuple

from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError

from Prog_12.models import Order, User, create_sync_session


class CRUDOrder:

    @staticmethod
    @create_sync_session
    def add(is_pad: bool, user_id: int = None, session: Session = None) -> Optional[Order]:
        order = Order(
            is_pad=is_pad,
            user_id=user_id
        )
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(order)
            return order

    @staticmethod
    @create_sync_session
    def get(order_id: int, session: Session = None) -> Optional[Order]:
        order = session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return order[0]

    @staticmethod
    @create_sync_session
    def all(user_id: int = None, session: Session = None) -> List[Order]:
        if user_id:
            orders = session.execute(
                select(Order).where(Order.user_id == user_id)
                .order_by(Order.id)
            )
        else:
            orders = session.execute(
                select(Order)
                .order_by(Order.id)
            )
        return [order[0] for order in orders]

    @staticmethod
    @create_sync_session
    def delete(order_id: int, session: Session = None) -> None:
        session.execute(
            delete(Order)
            .where(Order.id == order_id)
        )
        session.commit()

    @staticmethod
    @create_sync_session
    def update(
            order_id: int,
            date_created: str = None,
            user_id: int = None,
            is_pad: bool = None,
            session: Session = None
    ) -> bool:
        if is_pad or user_id or date_created:
            session.execute(
                update(Order)
                .where(Order.id == order_id)
                .values(
                    is_pad=is_pad if is_pad else Order.is_pad,
                    user_id=user_id if user_id else Order.user_id,
                    date_created=date_created if date_created else Order.date_created
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
    def join(order_id: int = None, session: Session = None) -> List[Tuple[Order, User]]:
        if order_id:
            response = session.execute(
                select(Order, User)
                .join(User, Order.id == User.order_id)
                .where(Order.id == order_id)
            )
        else:
            response = session.execute(
                select(Order, User)
                .join(User, Order.id == User.order_id)
                )
        return response.all()
