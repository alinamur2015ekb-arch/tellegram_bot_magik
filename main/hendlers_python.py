from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from .keyboard import python
from aiogram.fsm.context import FSMContext
from state.state import python1, python2, python3
from database import create_answer

router = Router()
one_python_answer = ["1", "3", "3", "2", "1"]
two_python_answer = ["1", "2", "3", "3", "1"]
three_python_answer = ["3", "2", "2", "1", "1"]

@router.message(Command("python"))
async def python(message:Message):
    await message.answer("Выберите уровень сложности", reply_markup=python)

#уровень 1
@router.callback_query(F.data=="one_python")
async def one_python(message: Message, state: FSMContext, callback: CallbackQuery):
    await callback.message.answer("Python уровень Легкий \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Какая функция выводит текст в консоль \n 1.) print()\n 2.) input() \n 3.) log()")
    await state.set_state(python1.a3)
    await callback.answer()

@router.message(python1.a3)
async def a3(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Какая функция запрашивает данные \n 1.) print()\n 2.) request()\n3.) input()")
    await state.set_state(python1.b3)

@router.message(python1.b3)
async def b3(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Какая функция может выводить что то бесконечное количество \n 1.)for \n 2.)infinity \n3.) while")
    await state.set_state(python1.c3)

@router.message(python1.c3)
async def c3(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Какая функция может что-то выводить определеное количество раз \n 1.) while\n 2.) for\n3.) infinity")
    await state.set_state(python1.d3)

@router.message(python1.d3)
async def d3(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n  Какая функция рандомно что-то генерирует\n 1.) randing\n 2.) random\n3.) rand ")
    await state.set_state(python1.e3)
    count_python1 = 0
    data3 = await state.get_data()
    
    a3=data3.get("a3"), 
    b3=data3.get("b3"), 
    c3=data3.get("c3"),
    d3=data3.get("d3"),
    e3=data3.get("e3")

    if a3 == one_python_answer[0]:
        count_python1 += 1
    if b3 == one_python_answer[1]:
        count_python1 += 1
    if c3 == one_python_answer[2]:
        count_python1 += 1
    if d3 == one_python_answer[3]:
        count_python1 += 1
    if e3 == one_python_answer[4]:
        count_python1 += 1
    await message.answer(f"У вас {count_python1}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")

    await create_answer(
        answer_python1 = count_python1
    )
    await state.clear()


#уровень 2

@router.callback_query(F.data=="two_python")
async def one_python(message: Message, state: FSMContext, callback: CallbackQuery):
    await callback.message.answer("Python уровень Средний \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Какая функция дабовляет что-то в конец списка \n 1.) .append\n 2.) .pop\n 3.) .ending")
    await state.set_state(python2.a4)
    await callback.answer()

@router.message(python2.a4)
async def a4(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Какая функция делает так чтобы в for что то выводилось несколько раз\n 1.) several\n 2.) range\n3.) once")
    await state.set_state(python2.b4)

@router.message(python2.b4)
async def b4(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Как сделать так чтобы цикл while был бесконечным \n 1.)while False \n 2.)while infinite\n3.) while True")
    await state.set_state(python2.c4)

@router.message(python2.c4)
async def c4(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Чем отличается кортеж от списка \n 1.) В нем () скобки\n 2.) В нем {} скобки\n3.) Он не изменяется")
    await state.set_state(python2.d4)

@router.message(python2.d4)
async def d4(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n Какая функция что то рандомно выбирает \n 1.) randint\n 2.) random\n3.) rand")
    await state.set_state(python2.e4)
    count_python2 = 0
    data3 = await state.get_data()
    
    a4=data3.get("a4"), 
    b4=data3.get("b4"), 
    c4=data3.get("c4"),
    d4=data3.get("d4"),
    e4=data3.get("e4")

    if a4 == two_python_answer[0]:
        count_python2 += 1
    if b4 == two_python_answer[1]:
        count_python2 += 1
    if c4 == two_python_answer[2]:
        count_python2 += 1
    if d4 == two_python_answer[3]:
        count_python2 += 1
    if e4 == two_python_answer[4]:
        count_python2 += 1
    await message.answer(f"У вас {count_python2}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")

    await create_answer(
        answer_python2 = count_python2
    )
    await state.clear()

#уровень 3

@router.callback_query(F.data=="three_python")
async def one_python(message: Message, state: FSMContext, callback: CallbackQuery):
    await callback.message.answer("Python уровень Сложный \n\n В ответ писать только цифры правильного ответа")
    await callback.message.answer("1 вопрос \n\n Как создать функцию \n 1.) funcio \n 2.) funkcion \n 3.) def")
    await state.set_state(python3.a5)
    await callback.answer()

@router.message(python3.a5)
async def a5(message:Message, state: FSMContext):
    await message.answer("2 вопрос \n\n Как в списке отсортировать элементы \n 1.) sert\n 2.) sort\n3.) sorting")
    await state.set_state(python3.b5)


@router.message(python3.b5)
async def b5(message:Message, state: FSMContext):
    await message.answer("3 вопрос \n\n Как объявить класс \n 1.)objekt \n 2.)class \n3.) close")
    await state.set_state(python3.c5)


@router.message(python3.c5)
async def c5(message:Message, state: FSMContext):
    await message.answer("4 вопрос \n\n Как вытощить что-то из списка \n 1.) По индексу\n 2.) По ключу\n3.) По значению")
    await state.set_state(python3.d5)

@router.message(python3.d5)
async def d5(message:Message, state: FSMContext):
    await message.answer("5 вопрос \n\n Какой командой что-то установить \n 1.) pip \n2.)establish \n3.) installation")
    await state.set_state(python3.e5)
    count_python3 = 0
    data5 = await state.get_data()
    
    a5=data5.get("a5"), 
    b5=data5.get("b5"), 
    c5=data5.get("c5"),
    d5=data5.get("d5"),
    e5=data5.get("e5")

    if a5 == three_python_answer[0]:
        count_python3 += 1
    if b5 == three_python_answer[1]:
        count_python3 += 1
    if c5 == three_python_answer[2]:
        count_python3 += 1
    if d5 == three_python_answer[3]:
        count_python3 += 1
    if e5 == three_python_answer[4]:
        count_python3 += 1
    await message.answer(f"У вас {count_python3}/5 <b>правильных</b> ответов.",
               parse_mode="HTML")


    await create_answer(
        answer_python3 = count_python3
    )
    await state.clear()