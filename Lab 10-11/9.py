import psycopg2
from config import config

def delete_user(user_id, name):
    sql = """
    delete from accounts where user_id=2
    """
    conn = None
    deleted_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, user_id))
        deleted_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

delete_user(2, 'Askar')