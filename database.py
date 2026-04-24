import sqlite3

def create_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login VARCHAR(1000) NOT NULL DEFAULT'',
        password VARCHAR(1000) NOT NULL DEFAULT''
    )
    """
    cursor.execute(sql)
    sql = """
    CREATE TABLE IF NOT EXISTS picture(
        id INTEGER PTIMARY KEY AUTOINCREMENT,
        picture_link VARCHAR(1000) NOT NULL DEFAULT'',
        user_id INTEGER,
        FOREIGN_KEY(user_id) REFERENCES user(id)
    )
    """

if __name__ == "__main__":
    create_db()