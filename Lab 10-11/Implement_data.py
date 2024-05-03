import psycopg2

conn = psycopg2.connect("dbname=test user=postgres password=pCak)B*a")
cursor = conn.cursor()

name = input("Enter name: ")
number = input("Enter phone number: ")

cursor.execute("INSERT INTO notebook (name, numbers) VALUES (%s, %s)", (name, number))

conn.commit()
cursor.close()
conn.close()