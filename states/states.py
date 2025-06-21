from aiogram.fsm.state import State, StatesGroup


class AddProduct(StatesGroup):
    product = State()
    price = State()
    confirm = State()
class RemoveProduct(StatesGroup):
    product_id = State()
    confirm = State()
class SearchProduct(StatesGroup):
    product_name = State()