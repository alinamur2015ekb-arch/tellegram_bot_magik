import aiosqlite
from typing import Optional

DB_NAME = "database.db"

async def init_answer():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS answer(
                    id PRIMARY KEY,
                    answer_math1 INTEGER,
                    answer_math2 INTEGER,
                    answer_math3 INTEGER,
                    answer_python1 INTEGER,
                    answer_python2 INTEGER,
                    answer_python3 INTEGER,
                    answer_robotics1 INTEGER,
                    answer_robotics2 INTEGER,
                        )
''')
    await db.commit()


async def create_answer(answer_math1, answer_math2, answer_math3, answer_python1, answer_python2, answer_python3, answer_robotics1, answer_robotics2):
    async with aiosqlite.connect(DB_NAME) as db: 
        await db.execute('''
    INSERT INTO answer (answer_math1, answer_math2, answer_math3, 
                        answer_python1, answer_python2, answer_python3, 
                        answer_robotics1, answer_robotics2) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (answer_math1, answer_math2, answer_math3, answer_python1, answer_python2, answer_python3, answer_robotics1, answer_robotics2))
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
                        id PRIMARY KEY,
                        random INTEGER,
                        meme INTEGER
                        )
''')
        await db.commit
        
async def create_play(random, meme):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(''' 
        INSERT INTO plsy_static (random, meme)
        VALUES (?, ?)
''', (random, meme))
        await db.commit()


async def get_answer_by_id(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM answer WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result


async def get_play_by_id(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute('SELECT * FROM play_static WHERE id = ?', (user_id,)) as cursor:
            result = await cursor.fetchone() 
            return result