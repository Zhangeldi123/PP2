import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='pCak)B*a'
)
current = config.cursor()
sql = '''
    INSERT INTO notebook
    VALUES (%s, %s, %s)
'''
config.commit()
current.close()
config.close()