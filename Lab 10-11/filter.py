import psycopg2

conn = psycopg2.connect("dbname=test user=postgres password=pCak)B*a")
cursor = conn.cursor()

# Query all data
cursor.execute("SELECT * FROM notebook;")
all_rows = cursor.fetchall()
for row in all_rows:
    print(row)

# Query data with a filter
filter_name = input("Enter the name to filter by: ")
cursor.execute("SELECT * FROM notebook WHERE name = %s", (filter_name,))
filtered_rows = cursor.fetchall()
for row in filtered_rows:
    print(row)

conn.commit()
cursor.close()
conn.close()