from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from .keyboard import math
from state.state import math1, math2, math3
from aiogram.fsm.context import FSMContext
from database import create_answer
            
router = Router()
answers_math1 = ["56", '5', '230', '16', '13']
answers_math2 = ['1/5', '10/2', '5/3', '5/4', '6/4']
answers_math3 = ['16', '3', '2.5', '15', '3']
@router.message(CommandStart())
async def start(message: Message):
    await message.answer("<b>Команды</b> \n\n Образовательные функций \n\n /mathematics \n /python \n /robotics " \
    "\n\n Развлекательные функций \n /random \n /funny_photos \n /mems \n /quest \n /player \n\n Статистика \n /my_education \n /my_play",
    parse_mode="HTML")


@router.message(Command("mathematics"))
async def mathes(message: Message):
    await message.answer("Выберите уровень сложности",
                        reply_markup=math)
    
#уровень 1
@router.callback_query(F.data == "one_math")
async def one(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Викторина по математике уровень легкий")
    await callback.message.answer("<b>1 вопрос </b> \n 8 * 7",
                            parse_mode="HTML")
    await state.set_state(math1.a)
    await callback.answer()


@router.message(math1.a, F.text)
async def a(message: Message, state: FSMContext):
    message.answer("<b> 2 вопрос </b> 45/9",
                   parse_mode="HTML")
    await state.set_state(math1.b)


@router.message(math1.b, F.text)
async def b(message: Message, state: FSMContext):
    await message.answer("<b> 3 вопрос </b> 23 * 10",
                   parse_mode="HTML")
    await state.set_state(math1.c)

@router.message(math1.c, F.text)
async def c(message: Message, state: FSMContext):
    await message.answer("<b> 4 вопрос </b> 48/3",
                   parse_mode="HTML")
    await state.set_state(math1.d)

@router.message(math1.d, F.text)
async def d(message: Message, state: FSMContext):
    await message.answer("<b> 5 вопрос </b> 52/4")
    await state.set_state(math1.e)
    count_math1 = 0
    data1 = await state.get_data()
    
    a=data1.get("a"), 
    b=data1.get("b"), 
    c=data1.get("c"),
    d=data1.get("d"),
    e=data1.get("e")
    
    if a == answers_math1[0]:
        count_math1 += 1
    if b == answers_math1[1]:
        count_math1 += 1
    if c == answers_math1[2]:
        count_math1 += 1
    if d == answers_math1[3]:
        count_math1 += 1
    if e == answers_math1[4]:
        count_math1 += 1

    await message.answer(f"У вас {count_math1}/5 <b>правильных</b> ответов.",
                   parse_mode="HTML")
    
    await create_answer(
        answer_math1 = count_math1
    )
    await state.clear()

#уровень 2
@router.callback_query(F.data == "two_math")
async def two(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Викторина по математике уровень средний")
    await callback.message.answer("<b>1 вопрос </b> \n Сократи дробь 6/30 до самой маленькой возможной дроби",
                            parse_mode="HTML")
    await state.set_state(math2.a1)
    await callback.answer()


@router.message(math2.a1, F.text)
async def a1(message: Message, state: FSMContext):
    await message.answer("<b> 2 вопрос </b> Запиши число 5 дробью с числителем 10 ",
                   parse_mode="HTML")
    await state.set_state(math2.b1)


@router.message(math2.b1, F.text)
async def b1(message: Message, state: FSMContext):
    await message.answer("<b> 3 вопрос </b> 2/3 + 3/3",
                   parse_mode="HTML")
    await state.set_state(math2.c1)


@router.message(math2.c1, F.text)
async def c1(message: Message, state: FSMContext):
    await message.answer("<b> 4 вопрос </b> 10/4 - 5/4",
                   parse_mode="HTML")
    await state.set_state(math2.d1)


@router.message(math2.d1, F.text)
async def d1(message: Message, state: FSMContext):
    await message.answer("<b> 5 вопрос </b> 2/2 * 3/2")
    await state.set_state(math2.e1)
    count_math2 = 0
    data2 = await state.get_data()
    
    a1=data2.get("a1"), 
    b1=data2.get("b1"), 
    c1=data2.get("c1"),
    d1=data2.get("d1"),
    e1=data2.get("e1")
    
    if a1 == answers_math2[0]:
        count_math2 += 1
    if b1 == answers_math2[1]:
        count_math2 += 1
    if c1 == answers_math2[2]:
        count_math2 += 1
    if d1 == answers_math2[3]:
        count_math2 += 1
    if e1 == answers_math2[4]:
        count_math2 += 1


    await message.answer(f"У вас {count_math2}/5 <b>правильных</b> ответов.",
                   parse_mode="HTML")
    
    await create_answer(
        answer_math2 = count_math2
    )
    await state.clear()

#уровень 3    
@router.callback_query(F.data == "three_math")
async def one(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Викторина по математике уровень сложный")
    await callback.message.answer("<b>1 вопрос </b> \n 2 в 4 степени",
                            parse_mode="HTML")
    await state.set_state(math3.a2)
    await callback.answer()


@router.message(math3.a2, F.text)
async def a2(message: Message, state: FSMContext):
    await message.answer("<b> 2 вопрос </b> найди дискриминант в уравнений x в квадрате - 5x + 4 = 0",
                   parse_mode="HTML")
    await state.set_state(math3.b2)



@router.message(math3.b2, F.text)
async def b2(message: Message, state: FSMContext):
    await message.answer("<b> 3 вопрос </b> Найди корень из 6.25",
                   parse_mode="HTML")
    await state.set_state(math3.c2)


@router.message(math3.c2, F.text)
async def c2(message: Message, state: FSMContext):
    await message.answer("<b> 4 вопрос </b> Запишите число которому равняется x - x/10 = 3/2",
                   parse_mode="HTML")
    await state.set_state(math3.d2)


@router.message(math3.d2, F.text)
async def d2(message: Message, state: FSMContext):
    await message.answer("<b> 5 вопрос </b> log(2) = 8")
    await state.set_state(math3.e2)
    count_math3 = 0
    data2 = await state.get_data()
    
    a2=data2.get("a2"), 
    b2=data2.get("b2"), 
    c2=data2.get("c2"),
    d2=data2.get("d2"),
    e2=data2.get("e2")
    
    if a2 == answers_math3[0]:
        count_math3 += 1
    if b2 == answers_math3[1]:
        count_math3 += 1
    if c2 == answers_math3[2]:
        count_math3 += 1
    if d2 == answers_math3[3]:
        count_math3 += 1
    if e2 == answers_math3[4]:
        count_math3 += 1


    await message.answer(f"У вас {count_math3}/5 <b>правильных</b> ответов.",
                   parse_mode="HTML")
    
    await create_answer(
        answer_math3 = count_math3
    )
    await state.clear()