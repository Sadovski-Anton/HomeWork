# https://suppliers-api.wildberries.ru/swagger/index.html#/Marketplace/get_api_v2_supplies__id__orders
# GET
# ​/api​/v2​/supplies​/{id}​/orders
# Возвращает список заказов, закреплённых за поставкой

from enum import Enum
import json
from pydantic import BaseModel, Field


class Status(int, Enum):
    first: int = 1
    second: int = 2
    third: int = 3
    forth: int = 4

class Barcodes(BaseModel):
    num_1: int
    num_2: int
    num_3: int


class DeliveryType(int, Enum):
    number_1: int = 0
    number_2: int = 1


class Orders(BaseModel):
    orderId: int = Field(max_length=8)
    dateCreated: str
    storeId: int
    wbWhId: int
    pid: int
    officeAddress: str
    chrtId: str
    barcodes: Barcodes
    status: Status
    userStatus: Status
    rid: int
    totalPrice: int
    currencyCode: int
    orderUID: str
    deliveryType: DeliveryType
