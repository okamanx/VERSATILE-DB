import asyncio
import asyncpg
import sys
print(sys.executable)
async def test():
    conn = await asyncpg.connect(user='postgres', password='Aman1234', database='gujarat', host='localhost')
    print("Connected!")
    await conn.close()

asyncio.run(test())