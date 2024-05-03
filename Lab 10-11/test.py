import psycopg2

try:
    with psycopg2.connect(
        
    ) as conn:
        print('Connected to the PostgreSQL server.')
        return conn
except (psycopg2.DatabaseError, Exception) as error:
    print(error)