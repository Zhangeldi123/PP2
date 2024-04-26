import psycopg2
from config import config


def create_tables():
    commands = (
        """
        CREATE TABLE accounts (
          user_id serial PRIMARY KEY,
          name VARCHAR (50) UNIQUE NOT NULL,
          phone VARCHAR (255) UNIQUE NOT NULL
        );
        """,
        
    )

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()

create_tables()