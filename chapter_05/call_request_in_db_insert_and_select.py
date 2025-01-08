import asyncpg
import asyncio
from asyncpg import Record

async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='postgres', # Имя базы данных.
        password='postgres'
    )

    # Execute use when call INSERT, UPDATE, DELETE, CREATE TABLE
    await connection.execute("INSERT INFO brand VALUES(DEFAULT, 'Levies')")
    await connection.execute("INSERT INFO brand VALUES(DEFAULT, 'Seven')")

    brand_query = 'SELECT brand_id, brand_name FROM brand'
    # Use when SELECT
    results: list[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id={brand["brand_id"]}, name={brand["name"]}')
    
    await connection.close()

asyncio.run(main())

