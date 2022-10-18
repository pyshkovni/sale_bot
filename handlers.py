from aiogram.types import Message
from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

from main import dp, bot
from sql import add, buy

class DataInput(StatesGroup):
    s = State()
    b = State()

@dp.message_handler(commands='add')
async def ask_data(message: Message):
    await bot.send_message(message.from_user.id, 'Введите товар, название магазина и цену через \'; \'')
    await DataInput.s.set()

@dp.message_handler(state=DataInput.s)
async def add_cmd(message: Message, state: FSMContext):
    s = message.text.split('; ')
    await add(*s)
    await message.answer('Спасибо. Запись успешно добавлена!')
    await state.finish()

@dp.message_handler(commands='show')
async def ask_data(message: Message):
    await bot.send_message(message.from_user.id, 'Введите название магазина.\nДля выбора всего ассортимента введите \'*\'')
    await DataInput.b.set()

@dp.message_handler(state=DataInput.b)
async def add_cmd(message: Message, state: FSMContext):
    b = message.text
    await message.answer(await buy(b))
    await state.finish()
    