import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='pCak)B*a'
)
current = config.cursor()
current.execute(
    '''
    CREATE TABLE notebook(
        id INT,
        numbers VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        email VARCHAR (20) );

    '''
)
config.commit()
current.close()
config.close()