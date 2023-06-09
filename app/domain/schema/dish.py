from pydantic import BaseModel


class Dish(BaseModel):
    dish_name: str
