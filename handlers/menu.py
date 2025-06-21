from aiogram import Router, F
from aiogram.filters import state
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.reply import confirm_button, menu_buttons
from states.states import AddProduct, RemoveProduct, SearchProduct
from utils.db import Products, session

menu_router = Router()

@menu_router.message(F.text == 'add product')
async def product_handler(message: Message , state: FSMContext) -> None:
    await message.answer('Mahsulotning nomini yozing' , reply_markup=ReplyKeyboardRemove())
    await state.set_state(AddProduct.product)
@menu_router.message(AddProduct.product)
async def summa_handler(message: Message , state: FSMContext) -> None:
    product = message.text
    await state.update_data(product=product)
    await message.answer('summasini kiriting: ')
    await state.set_state(AddProduct.price)
@menu_router.message(AddProduct.price)
async def summa_handler(message: Message , state: FSMContext) -> None:
    price = message.text
    datas = await state.get_data()
    await state.update_data(summa=price)
    product = datas.get('product')
    await message.answer(f'tasdiqlaysizmi: \n'
                         f'Mahsulot-> {product}\n'
                         f'Summasi -> {price}' , reply_markup=confirm_button())
    await state.set_state(AddProduct.confirm)

@menu_router.message(AddProduct.confirm)
async def confirm_handler(message: Message , state: FSMContext) -> None:
    confirm = message.text
    datas = await state.get_data()
    await state.update_data(confirm=confirm)

    if confirm.casefold() == 'ha':
        product = Products(name=datas.get('product'), price=datas.get('summa'))
        product.save(session)
        await message.answer('Mahsulot qoshildi' , reply_markup=menu_buttons())
        await state.clear()
    elif confirm.casefold() == 'yoq':
        await message.answer('Menuga qaytdingiz' , reply_markup=menu_buttons())
    else:
        await message.answer('Ha yoki yo`q tugamsini bosing')


@menu_router.message(F.text == 'delete product')
async def delete_handler(message: Message , state: FSMContext) -> None:
    await message.answer('Mahsulotning id isini kiriting')
    await state.set_state(RemoveProduct.product_id)
@menu_router.message(RemoveProduct.product_id)
async def confirm_handler(message: Message , state: FSMContext) -> None:
    product_id = message.text
    await state.update_data(product_id=product_id)
    await message.answer('Tasdiqlaysizmi?' , reply_markup=confirm_button())
    await state.set_state(RemoveProduct.confirm)
@menu_router.message(RemoveProduct.confirm)
async def confirm_handler1(message: Message , state: FSMContext) -> None:
    confirm = message.text
    datas = await state.get_data()
    await state.update_data(confirm=confirm)
    if confirm.casefold() == 'ha':
        product = Products()
        product.delete(session , datas.get('product_id'))
        await state.clear()
        await message.answer('Mahsulot o`chirildi' , reply_markup=menu_buttons())
    elif confirm.casefold() == 'yoq':
        await message.answer('Menuga qaytdingiz' , reply_markup=menu_buttons())
        await state.clear()
    else:
        await message.answer('Ha yoki yo`q tugamsini bosing')
@menu_router.message(F.text == 'search')
async def search_handler(message: Message , state: FSMContext) -> None:
    await message.answer('Mahsulotning nomini yozing' , reply_markup=ReplyKeyboardRemove())
    await state.set_state(SearchProduct.product_name)
@menu_router.message(SearchProduct.product_name)
async def search_handler(message: Message) -> None:
    product_name = message.text

    product1 = Products()
    result = product1.search_product(product_name , session)
    if result:
        await message.answer('Mahsulot mavjud' , reply_markup=menu_buttons())
    else:
        await message.answer('Mahsulot topilmadi' ,  reply_markup=menu_buttons())