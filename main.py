import psycopg2, os
from dotenv import load_dotenv

load_dotenv()

try:
    connection = psycopg2.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DB_NAME'),
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT version();'
        )
        print(f'Server version: {cursor.fetchone()}')

    with connection.cursor() as cursor:
        cursor.execute(
            '''CREATE TABLE cars(
                id serial PRIMARY KEY,
                brand varchar(64) NOT NULL,
                model varchar(64) NOT NULL,
                price int NOT NULL,
                lastouner varchar(64)
            );'''
        )
        print('[INFO] Table created successfully')

    with connection.cursor() as cursor:
        cursor.execute(
            '''INSERT INTO cars (brand, model, price) VALUES
            ('Hyndai', 'Creta', 2200000);
            '''
        )
        print('[INFO] Data was succefully inserted')

    with connection.cursor() as cursor:
        cursor.execute(
            '''SELECT model FROM cars WHERE brand = 'Hyndai';'''
        )
        print(f'{cursor.fetchone()}')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] PostgreSQL connection closed')


