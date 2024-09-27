import random
import time
from random import randint
import ramapi
import aiofiles
import requests
from aiogram.exceptions import TelegramBadRequest

from config import Kiber1
from config import Kiber
from config import Kiber2
from config import Kiber3
from config import Form
from aiogram import Bot, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile
from aiogram.types import Message, CallbackQuery
from fitst_bot.keyboard import first_k, msg_k, number_k
from fitst_bot.config import Auto
from main import dp
from aiogram.types import URLInputFile
import requests
from aiogram.types import InputMediaPhoto
import asyncio


# @dp.message()
# async def wasd(message: Message, bot: Bot):
#     print('vavavava')
#     print(message)
#     await message.answer(message.audio.file_id)
#     #await bot.send_audio(message.from_user.id, 'CQACAgIAAxkBAAOFZdG38Ql4Lcz-ESJ9G7EfvJWEo88AAlE8AALAuJBKzFOlwqzQI_E0BA')
@dp.message(Command('start'))
async def startyyy(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    global chatik_ID
    chatik_ID = message.chat.id
    await bot.send_message(message.chat.id, text='Самый лучший бот', reply_markup=msg_k)


@dp.message(Command("dog"))
async def cmd_start111(message: Message, state: FSMContext, bot: Bot):
    await bot.send_photo(message.chat.id,
                         photo='https://img.freepik.com/free-photo/beautiful-pet-portrait-of-dog_23-2149218450.jpg')




@dp.message(Command('music'))
async def music(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           'что вы хотите?',
                           reply_markup=number_k)


@dp.callback_query(F.data == 'add music')
async def music11(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, 'введите название песни')
    await state.set_state(Kiber2.name)


@dp.message(Kiber2.name)
async def music111(message: Message, state: FSMContext, bot: Bot):
    f = open('file1.txt', 'a')
    f.write(message.text + '\n')
    print(type(message.text))
    await bot.send_message(message.from_user.id, 'отправьте музыку')
    await state.set_state(Kiber2.name1)


@dp.message(Kiber2.name1)
async def music1111(message: Message, state: FSMContext, bot: Bot):
    f = open('file.txt', 'a')
    f.write(message.audio.file_id + '\n')
    await bot.send_message(message.from_user.id, 'вы добавили песню')
    await state.clear()


@dp.callback_query(F.data == 'music1')
async def music1(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,'что желаете', reply_markup=number_k)

@dp.callback_query(F.data == 'music')
async def music(message: Message, state: FSMContext, bot: Bot):
    f = open('file1.txt', 'r')
    await bot.send_message(message.from_user.id,
                           'введите назвние песни\n\nДоступные песни:\nбравл\nДевочка\nКарнавал\nсигма крипер\nсигма крутой\nФедерико\nя кольт\n\nили введите строку загрузок\n' + f.read())
    await state.set_state(Kiber3.name)


@dp.message(Kiber3.name)
async def music1(message: Message, state: FSMContext, bot: Bot):
    global path
    print(message.text)
    f = open('file.txt', 'r')
    a = f.readlines()
    if a in wsedo100: path = a[int(message.text)]
    if message.text == 'бравл': path = 'CQACAgIAAxkBAAOLZdG4wursW2d_svHT2-B_UrqMCL0AAlo8AALAuJBKVRzCnNXyT7Q0BA'
    if message.text == 'Девочка': path = 'CQACAgIAAxkBAAONZdG41ANjI7aMnI7z_BMjuTCIyX4AAls8AALAuJBKITT9NvlAB5M0BA'
    if message.text == 'Карнавал': path = 'CQACAgIAAxkBAAOPZdG43zeM5emeN9AAAbgFzCukO2_rAAJcPAACwLiQSs5LRcxh2sNANAQ'
    if message.text == 'сигма крутой': path = 'CQACAgIAAxkBAAORZdG4560edsehvZy2pnjS6j4ECI0AAl48AALAuJBKwhyqgCTyxnU0BA'
    if message.text == 'сигма крипер': path = 'CQACAgIAAxkBAAOFZdG38Ql4Lcz-ESJ9G7EfvJWEo88AAlE8AALAuJBKzFOlwqzQI_E0BA'
    if message.text == 'Федерико': path = 'CQACAgIAAxkBAAOTZdG48-ljMuJcpxiwE8z-VPiKCrYAAl88AALAuJBKltBoQ8OFghQ0BA'
    if message.text == 'я кольт': path = 'CQACAgIAAxkBAAOXZdG5GAF0LLsq9CKsYcxxn_30dooAAmI8AALAuJBK2pP5WQ3qS4s0BA'

    await bot.send_audio(message.from_user.id, audio=path)
    await state.clear()


@dp.message(Command('start'))
async def startyyy(message: Message, state: FSMContext, bot: Bot):
    global chatik_ID
    chatik_ID = message.chat.id
    await bot.send_message(message.chat.id, text='Самый лучший бот', reply_markup=msg_k)


@dp.callback_query(F.data == 'sigma')
async def cmd_start11111(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global photo_sigma
    ran = random.randint(1, 5)

    if ran == 1: photo_sigma = 'https://i1.sndcdn.com/artworks-SP4zAuyzKul0x4Ed-F01JAA-t500x500.jpg'
    if ran == 2: photo_sigma = 'https://st-1.akipress.org/cdn-st-0/qdO/P/1690279277_0.jpg'
    if ran == 3: photo_sigma = 'https://i1.sndcdn.com/artworks-fTyLanyIekdUXec3-4P5inA-t500x500.jpg'
    if ran == 4: photo_sigma = 'https://opis-cdn.tinkoffjournal.ru/mercury/main-mem2023.1tmlo3..jpg'
    if ran == 5: photo_sigma = 'https://avatars.dzeninfra.ru/get-zen_doc/9632065/pub_6421b26a70ddc014c1c306d4_6421b2fc9ad2261bc2a48db1/scale_1200'
    print(ran, photo_sigma)
    await bot.send_photo(chat_id=callback.from_user.id, photo=photo_sigma)


@dp.callback_query(F.data == 'anime')
async def cmd_start11(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id, text='Введите аттрибут для поиска на английском')
    await state.set_state(Kiber1.name)


@dp.message(Kiber1.name)
async def rick(message: Message, state: FSMContext, bot: Bot):
    req = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={message.text}')
    data = req.json()
    for namesss in data['data']:
        await bot.send_message(chat_id=message.from_user.id, text=namesss['attributes']['slug'])
    await state.clear()


@dp.callback_query(F.data == 'rick and morty')
async def cmd_start111(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id, text='Введите имя персонажа на английском')

    await state.set_state(Kiber.name)


@dp.message(Kiber.name)
async def rick(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id, text='Введите dead или live ваш персонаж')
    await state.update_data(pers=message.text)
    await state.set_state(Kiber.name1)


@dp.message(Kiber.name1)
async def morty(message: Message, state: FSMContext, bot: Bot):
    data11 = await state.get_data()
    data1111 = ramapi.Character.filter(name=data11['pers'],
                                       status=message.text)
    for namesss in data1111['results']:
        await bot.send_message(chat_id=message.from_user.id, text=namesss['name'])
        await bot.send_photo(chat_id=message.from_user.id, photo=namesss['image'])
        print(namesss)

    await state.clear()


# @dp.message(Command("start"))
# async def cmd_start(message: Message, state: FSMContext, bot: Bot):
#     print('srabotalo 1', message)
#     await message.answer(text="Вот функционал бота: /sigma")
#     await state.set_state()


ggwp = [0, 10]

wsedo100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
            84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


@dp.callback_query(F.data == 'weather')
async def profile(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=callback.from_user.id, text='введите ваш город на английском с большой буквы')
    await state.set_state(Form.age)


@dp.message(Form.age)
async def profile(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(chat_id=message.from_user.id,
                           text='введите номер, чтобы узнать\n1-город\n2-страну\n3-температуру\n4-скорость ветра\n5-время')
    await state.update_data(city=message.text)
    print(message.text)
    await state.set_state(Form.name)


@dp.message(Form.name)
async def age(message: Message, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    req = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key=e90a7d854e9a4e2698393658242701&q={data1['city']}&aqi=no")
    data = req.json()
    print('data:::', data)
    mmm = list(message.text)
    print(message.text, mmm)

    city = data['location']['name']
    country = data['location']['country']
    temp = data["current"]["temp_c"]
    wind = data["current"]["wind_mph"]
    timee = data['location']['localtime']

    if '1' in mmm: await bot.send_message(chat_id=message.from_user.id, text=f'город - {city}')
    if '2' in mmm: await bot.send_message(chat_id=message.from_user.id, text=f'страна - {country}')
    if '3' in mmm: await bot.send_message(chat_id=message.from_user.id, text=f'температура - {temp}')
    if '4' in mmm: await bot.send_message(chat_id=message.from_user.id, text=f'ветер - {wind}')
    if '5' in mmm: await bot.send_message(chat_id=message.from_user.id, text=f'время - {timee}')

    if temp < 5:
        await bot.send_message(chat_id=message.from_user.id, text='холодно,останьтесь дома')
    else:
        await bot.send_message(chat_id=message.from_user.id, text='иди в школу')
    print(message.text)
    await state.clear()


#
# @dp.message(Form.age)
# async def age(message: Message, state: FSMContext, bot: Bot):
#     await bot.send_message(chat_id=message.chat.id, text='введите  ваш пол')
#     await state.set_state(Form.about)
#
#
# @dp.message(Form.about)
# async def age(message: Message, state: FSMContext, bot: Bot):
#     await bot.send_message(chat_id=message.chat.id, text='расскажите о себе')
#     data = await state.get_data()
#     print('data:::', data)
#     await state.clear()
#     formatted_text = ''
#     for key, value in data.items():
#         formatted_text += f'{key}: {value}'
#     print(formatted_text)


# @dp.message((F.text == "/admin"))
# async def click_button(message: Message,bot:Bot):
#     a = 5
#     c: float = 1
#
#     await message.answer(text="1")
#
#     while c < float(a):
#         time.sleep(1)
#         c += 1
#         d = str(c)
#         await message.answer(text=d)
#     await message.answer(text="Приветствую администратора")
@dp.message(Command('clear'))
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        # Если сообщение не найдено (уже удалено или не существует),
        # код ошибки будет "Bad Request: message to delete not found"
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")


@dp.message(F.text.in_({'рандом', 'рандом 2'}))
async def click_button(message: Message):
    await message.answer(text="Нажмите на кнопку чтобы получить рандомное число", reply_markup=msg_k)


async def send_photo(bot: Bot, photo, chat_id):
    await bot.send_photo(chat_id=chat_id, photo=photo, caption='Вот ваша фотография')


@dp.message(Auto.engine, F.photo)
async def get_photo(message: Message, bot: Bot):
    photo = message.photo[-1].file_id
    await message.answer(text="Отлично, вы отправили фото")
    await send_photo(bot, photo, message.from_user.id)


@dp.message(F.text)
async def error_msg(message: Message, bot: Bot, state: FSMContext):
    price = await state.get_data()
    print(price.get("price"))
    await bot.send_message(chat_id=message.from_user.id, text="Вы ввели неизвестную команду")


async def edit_msg(message: Message):
    await message.edit_text(text="Текст был изменен", reply_markup=msg_k)


@dp.callback_query(F.data == 'random_num')
async def send_random_value(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            "price": callback.message.text
        }
    )
    await edit_msg(callback.message)
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer(
        text="Спасибо за использование бота!",
        show_alert=True
    )
