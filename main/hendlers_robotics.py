from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from .keyboard import robotics
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from state.state import robotics1, robotics2
from database import create_answer

router = Router()
one_robotics_answer = ["2", "1", "3"]
two_robotics_answer = ["2", "1", "2"]

@router.message(Command("robotics"))
async def roborics(message: Message):
    await message.answer("Выберите уровень сложности",
                         reply_markup=robotics)

# 1 уровень
@router.callback_query(F.data == "one_robotics")
async def one_robotics(state: FSMContext, callback: CallbackQuery):
    await callback.message.answer("Робототехника на arduino. <b>Уровень Легкий.</b> Писать только номер ответа\n\n 1 вопрос Где пишется код для arduino?\n 1.) python\n 2.) Arduino IDE\n 3.) C#",
                                  parse_mode="HTML")
    await state.set_state(robotics1.a6)
    await callback.answer()

@router.message(robotics1.a6, F.text)
async def a6(state: FSMContext, message: Message):
    await message.answer("2 вопрос Как называется код в arduino IDE?\n1.) Скетч\n2.) Кодот\n 3.) Arduino")
    await state.set_state(robotics1.b6)

@router.message(robotics1.b6, F.text)
async def b6(state: FSMContext, message: Message):
    await message.answer("3 вопрос Какие 2 функций обязательны в коде для arduino IDE?\n 1.) vood(), loop()\n setup(), lood()\n 3.) setup(), loop()")
    await state.set_state(robotics1.c6)
    one_count_robotics = 0
    data5 = await state.get_data()

    a6 = data5.get("a6"),
    b6 = data5.get("b6"),
    c6 = data5.get("c6")

    if a6 == one_robotics_answer[0]:
        one_count_robotics += 1
    if b6 == one_robotics_answer[1]:
        one_count_robotics += 1
    if c6 == one_robotics_answer[2]:
        one_count_robotics +=1

    await message.answer(f"У вас {one_count_robotics}/3 <b>правильных</b> ответов")

    await create_answer(
        answer_robotics1 = one_count_robotics
    )
    await state.clear()

# 2 уровень

@router.message(F.data == "two_robotics")
async def two_robotics(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Робототехника на arduino \n\n Уровень 2 - <b>Сложный</b> \n 1 вопрос Какой пин у встроеного светодиоида в плате arduino uno\n1.)12 \n2.)13 \n3.)10 ",
                                  parse_mode="HTML")

    await state.set_state(robotics2.a7)

    await callback.answer()

@router.message(robotics2.a7)
async def a7(message: Message, state: FSMContext):
    await message.answer("2 вопрос Как в коде прописать паузу в Arduino IDE \n1.) delay\n2.) pause\n3.) stop")

    await state.set_state(robotics2.b7)

@router.message(robotics2.b7)
async def b7(message: Message, state: FSMContext):
    await message.answer("3 вопрос Какое напрежение обычно в плате arduino\n1.) 13v \n2.) 5v \n3.) 220v ")

    await state.set_state(robotics2.c7)
    two_count_robotics = 0
    data6 = await state.get_data()

    a7 = data6.get("a7"),
    b7 = data6.get("b7"),
    c7 = data6.get("c7")

    if a7 == two_robotics_answer[0]:
        two_count_robotics += 1
    if b7 ==  two_robotics_answer[1]:
        two_count_robotics += 1
    if c7 == two_robotics_answer[2]:
        two_count_robotics += 1

    await message.answer(f"У вас {two_count_robotics}/3 <b>правильных</b> ответов")

    await create_answer(
        answer_robotics2=two_count_robotics
    )

    await state.clear()