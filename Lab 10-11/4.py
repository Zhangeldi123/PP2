import psycopg2
def get_connection():
	try:
		return psycopg2.connect(
			database="postgres",
			user="postgres",
			password="pCak)B*a",
			host="127.0.0.1",
			port=5432,
		)
	except:
		return False
conn = get_connection()
  
# CREATE A CURSOR USING THE CONNECTION OBJECT
curr = conn.cursor()
  
# EXECUTE THE SQL QUERY
curr.execute("SELECT * FROM notebook;")
  
# FETCH ALL THE ROWS FROM THE CURSOR
data = curr.fetchall()
  
# PRINT THE RECORDS
for row in data:
    print(row)
  
# CLOSE THE CONNECTION
conn.close()