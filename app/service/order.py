import random
import time

from fastapi import HTTPException
from service.base import Service

from module.redis.redis import RedisClient
from domain.schema.dish import Dish


class OrderService(Service):
    def __init__(self):
        self.order_queue = RedisClient().queue("order_queue")

    def query(self, order_id):
        job = self.order_queue.fetch_job(order_id)
        if not job:
            raise HTTPException(status_code=404, detail="Order not found")

        if job.get_status() == 'failed':
            raise HTTPException(status_code=500, detail="Job failed")

        if job.get_status() != 'finished':
            return {
                'status': job.get_status()
            }

        return {
            'status': job.get_status(),
            'result': job.result
        }

    def create(self, dish: Dish):
        job = self.order_queue.enqueue(process_order, dish.dish_name)
        return {'order_id': job.id}


dishes = {
        'pizza': '🍕',
        'pasta': '🍝',
        'salad': '🥗',
        'milkshake': '🥤',
        'coke': '🥤',
    }


def process_order(dish_name: str):
    time_lapsed = random.randint(1, 10)
    time.sleep(time_lapsed)
    cooked_dish = dishes.get(dish_name)
    if not cooked_dish:
        return 'Sorry, after checking with the kitchen we do not have that dish today'

    return f'Your {cooked_dish} is ready! It took {time_lapsed}s'
