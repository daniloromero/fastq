#!/usr/bin/python3
from models.base import BaseModel
from models.store import Store
from models.food import Food
from models.drink import Drink
from models.order import Order
from models.confirmation import Confirmation

my_model = Drink()
my_model.name = "Pola"
my_model1 = Order()
my_model1.order_number = 1
my_model2 = Confirmation()
my_model2.order_number = 1
my_model2.status = "payment completed"
my_model3 = Food()
my_model3.name = "Empanada"
#my_model.store_id = 'f2f4d135-d076-43b4-8c24-0a815df4e7c3' 
print(my_model)
print(my_model1)
print(my_model2)
print(my_model3)
my_model.save()
print(my_model)