import psycopg2
from config import config

def new(user_id, name):
    sql = """
    SELECT * FROM accounts
    WHERE user_id = 4;
    """
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

new(4,'askar')