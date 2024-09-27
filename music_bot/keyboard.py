from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

first_k = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='рандом'),
        KeyboardButton(text='рандом 2')
    ],
], resize_keyboard=True, input_field_placeholder="Вот ваши 2 кнопки")




msg_k = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='бахнуть сигму', callback_data='sigma',),
        InlineKeyboardButton(text='поиск аниме', callback_data='anime',),


    ],
    [
        InlineKeyboardButton(text='персонажи рик и морти', callback_data='rick and morty',),
        InlineKeyboardButton(text='погода', callback_data='weather', ),
    ],
    [
        InlineKeyboardButton(text='музыка', callback_data='music1'),
    ]

])

number_k = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='слушать', callback_data='music'),
        InlineKeyboardButton(text='добавить', callback_data='add music'),
    ]

])