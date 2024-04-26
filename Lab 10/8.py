import psycopg2
from config import config


def insert_account(name, phone):
    sql = """
    INSERT INTO accounts(name, phone)
    VALUES(%s, %s) RETURNING user_id;
    """

    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name, phone))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

    return user_id

insert_account("Dina", '8-700-000-00-08')
insert_account('askar', '8-777-777-77-77')
insert_account("John", '8-777-554-98-30')
insert_account('Andrew', '8-702-987-14-87')