import psycopg2

conn = psycopg2.connect("dbname=test user=postgres password=pCak)B*a")
cursor = conn.cursor()

new_name = input("Enter new name: ")
phone_number = input("Enter phone number of the user to update: ")

cursor.execute("UPDATE notebook SET name = %s WHERE numbers = %s", (new_name, phone_number))

conn.commit()
cursor.close()
conn.close()