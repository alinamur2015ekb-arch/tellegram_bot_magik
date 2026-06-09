import aiosqlite
from typing import Optional

DB_NAME = "database.db"

async def init_answer():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS answer(
                    # ID здесь оставлен для автоинкремента, но не привязан к user_id
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    answer_math1 INTEGER,
                    answer_math2 INTEGER,
                    answer_math3 INTEGER,
                    answer_python1 INTEGER,
                    answer_python2 INTEGER,
                    answer_python3 INTEGER,
                    answer_robotics1 INTEGER,
                    answer_robotics2 INTEGER
            )
        ''')
        await db.commit()

async def create_answer(
    answer_math1: Optional[int] = None, 
    answer_math2: Optional[int] = None, 
    answer_math3: Optional[int] = None, 
    answer_python1: Optional[int] = None, 
    answer_python2: Optional[int] = None, 
    answer_python3: Optional[int] = None, 
    answer_robotics1: Optional[int] = None, 
    answer_robotics2: Optional[int] = None
):
    async with aiosqlite.connect(DB_NAME) as db: 
        # Список полей для вставки
        fields = []
        # Список значений для вставки
        values = []
        # Список плейсхолдеров для SQL
        placeholders = []

        if answer_math1 is not None:
            fields.append("answer_math1")
            values.append(answer_math1)
            placeholders.append("?")
        if answer_math2 is not None:
            fields.append("answer_math2")
            values.append(answer_math2)
            placeholders.append("?")
        if answer_math3 is not None:
            fields.append("answer_math3")
            values.append(answer_math3)
            placeholders.append("?")
        if answer_python1 is not None:
            fields.append("answer_python1")
            values.append(answer_python1)
            placeholders.append("?")
        if answer_python2 is not None:
            fields.append("answer_python2")
            values.append(answer_python2)
            placeholders.append("?")
        if answer_python3 is not None:
            fields.append("answer_python3")
            values.append(answer_python3)
            placeholders.append("?")
        if answer_robotics1 is not None:
            fields.append("answer_robotics1")
            values.append(answer_robotics1)
            placeholders.append("?")
        if answer_robotics2 is not None:
            fields.append("answer_robotics2")
            values.append(answer_robotics2)
            placeholders.append("?")
        
        # Если хотя бы одно значение передано, выполняем INSERT
        if fields:
            query = f"INSERT INTO answer ({', '.join(fields)}) VALUES ({', '.join(placeholders)})"
            await db.execute(query, tuple(values))
            await db.commit()


async def get_answer():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM answer') as cursor:
            result = await cursor.fetchall()
            return result

# 2 бд
async def init_play():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(''' 
            CREATE TABLE IF NOT EXISTS play_static(
                        # ID здесь оставлен для автоинкремента
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        random INTEGER,
                        meme INTEGER
            )
        ''')
        await db.commit()
        
# Функция для создания новой записи в таблице игр
async def create_play(random: Optional[int] = None, meme: Optional[int] = None):
    async with aiosqlite.connect(DB_NAME) as db:
        fields = []
        values = []
        placeholders = []

        if random is not None:
            fields.append("random")
            values.append(random)
            placeholders.append("?")
        if meme is not None:
            fields.append("meme")
            values.append(meme)
            placeholders.append("?")
        
        if fields:
            query = f"INSERT INTO play_static ({', '.join(fields)}) VALUES ({', '.join(placeholders)})"
            await db.execute(query, tuple(values))
            await db.commit()


async def get_answer_by_id():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM answer WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result

async def get_play_by_id():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM play_static WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result
