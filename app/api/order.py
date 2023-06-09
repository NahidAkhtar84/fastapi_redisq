from fastapi import APIRouter, Depends

from domain.schema.dish import Dish
from service.order import OrderService

order = APIRouter()


@order.post("/order")
def submit_order(dish: Dish, service: OrderService = Depends(OrderService)) -> dict:
    return service.create(dish)


@order.get("/order/{order_id}")
def get_order_status(order_id: str,  service: OrderService = Depends(OrderService)):
    return service.query(order_id)
