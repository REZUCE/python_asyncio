import asyncpg
import asyncio
from command_create_table import (
    CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, 
    CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE, 
    CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT
)

async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='postgres', # Имя базы данных.
        password='postgres'
    )
    statements = [
        CREATE_BRAND_TABLE, CREATE_PRODUCT_TABLE, 
        CREATE_PRODUCT_COLOR_TABLE, CREATE_PRODUCT_SIZE_TABLE, 
        CREATE_SKU_TABLE, SIZE_INSERT, COLOR_INSERT
    ]
    print('Создание таблиц в базе данных products!')

    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('Таблицы созданы в базе данных products!')
    await connection.close()

asyncio.run(main())

