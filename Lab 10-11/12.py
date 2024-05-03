import psycopg2
def check_name(name):
    cur.execute("SELECT name, score, level from SNAKE")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            print(f'Hello, {name}. Your current score and level: {rows[1]}, {rows[2]}.')
            return False
    return True


def check_score(name):
    cur.execute("SELECT name, score, level from snake")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            if result[1] >= int(rows[2]) and result[0] > int(rows[1]):
                cur.execute(f"UPDATE SNAKE set score = {str(result[0])}, level = {str(result[1])} where name = '{name}'")
                con.commit()
                return True
    return False
global con, cur

con = psycopg2.connect(
    database='test',
    user='postgres',
    password='pCak)B*a',
    host="localhost",
    port="5432"
)
print('You have successfully connected to the databases')

cur = con.cursor()
# CREATE TABLE
# cur.execute('''DROP TABLE "SNAKE SCORE"''')
# cur.execute('''CREATE TABLE snake
#     (NAME TEXT PRIMARY KEY NOT NULL,
#     SCORE TEXT NOT NULL,
#     LEVEL TEXT NOT NULL);'''
# )

name = input('Input your name: ')


if check_name(name):
    cur.execute(f'''INSERT INTO SNAKE (name, score, level) VALUES('{name}', 0, 0)''')
    con.commit()
    print('You are a new player! Your username is added to the databases.')
    

main()
con.commit()
if check_score(name):
    print(f'Congratulations! You have achieved a new result: {score}.')

con.commit()