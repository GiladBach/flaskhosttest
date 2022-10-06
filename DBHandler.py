
import sqlite3

from consts import db_path

class DBHandler():

    def __init__(self):
        self.conn = sqlite3.connect(db_path)

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS USERS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME VARCHAR(30) UNIQUE NOT NULL,
                NICKNAME VARCHAR(30) NOT NULL
            )
        """)
        self.conn.commit()

    def get_nickname(self, username):
        print(username)
        print(self.conn.execute("""SELECT * FROM USERS""").fetchone())
        nickname = self.conn.execute("""
            SELECT NICKNAME FROM USERS WHERE USERNAME = :USERNAME
        """, {'USERNAME': username}).fetchone()
        print(nickname)
        return nickname[0]

    def clear_users(self):
        self.conn.execute("""DELETE FROM USERS""")

    def insert_user(self, username, nickname):
        print(username, nickname)
        self.conn.execute("""
            INSERT INTO USERS(USERNAME, NICKNAME) VALUES(:USERNAME, :NICKNAME)
        """, {'USERNAME': username, 'NICKNAME': nickname})
        self.conn.commit()