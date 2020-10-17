#!/usr/bin/python3
from models.base import BaseModel
from models.store import Store
from models.food import Food
from models.drink import Drink
from models.order import Order
from models import storage
from models.confirmation import Confirmation

my_store = Store(name="JV")
my_store.save()


my_food = Food(price=4000, store_id=my_store.id, name="Tinto")
my_food.save()

my_order = Order(order_number=1, food_id=my_food.id, store_id=my_store.id)
my_order.save()
all_order = storage.all(Order)

print(my_order)

print(my_store)

print(my_food)

# Link order with one food
my_order.foods.append(my_food)

storage.save()
print(all_order)
