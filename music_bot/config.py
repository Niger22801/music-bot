from aiogram.filters.state import State, StatesGroup


class Auto(StatesGroup):
    engine = State()
    wheel = State()
    body = State()

class Form(StatesGroup):
     name = State()
     age = State()
     pol = State()
     about = State()
     photo = State()


class Kiber(StatesGroup):
    name = State()
    name1 = State()
    name2 = State()

class Kiber1(StatesGroup):
    name = State()
    name1 = State()
    name2 = State()

class Kiber2(StatesGroup):
    name = State()
    name1 = State()
    name2 = State()

class Kiber3(StatesGroup):
    name = State()
    name1 = State()
    name2 = State()