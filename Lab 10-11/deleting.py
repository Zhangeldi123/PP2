import psycopg2

conn = psycopg2.connect("dbname=test user=postgres password=pCak)B*a")
cursor = conn.cursor()

delete_name = input("Enter the name of the user to delete: ")
delete_phone = input("Enter the phone number of the user to delete: ")

cursor.execute("DELETE FROM notebook WHERE name = %s OR numbers = %s", (delete_name, delete_phone))

conn.commit()
cursor.close()
conn.close()