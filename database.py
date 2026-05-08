import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_db():
    conn = sqlite3.connect("CAT_MEMES.db")
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
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            picture_link VARCHAR(1000) NOT NULL DEFAULT'',
            user_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    """

    cursor.execute(sql)
    conn.commit()

def add_user(login, password):
    conn = sqlite3.connect("CAT_MEMES.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)    
    
    cursor.execute('INSERT INTO user(login,password) VALUES(?,?)', (login, hashed_password))

def is_user_exists(login):
    conn = sqlite3.connect("CAT_MEMES.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user WHERE login = ?", (login,))
    user = cursor.fetchone()
    
    return user != None

if __name__ == "__main__":
    create_db()