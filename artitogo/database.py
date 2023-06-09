
import sqlite3


class Database:
    def __init__(self):
        self.data_con = sqlite3.connect('user.db')
        self.users = self.data_con.cursor()
        self.create_user_database()

    def create_user_database(self):
        # Creating Database

        self.users.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id TEXT NOT NULL,
            password TEXT NOT NULL
            )
            """)

        self.data_con.commit()

    def storeAcc(self, user, passw):

        self.users.execute("INSERT into users (user_id, password) values(?, ?)", (
            user,
            passw
        ))

        self.data_con.commit()

    def select_user(self):
        self.users.execute("SELECT user_id FROM users")

        data = self.users.fetchone()[0]

        return data

    def verifyAcc(self, passw):

        self.users.execute("SELECT password FROM users")

        verify_password = self.users.fetchone()[0]
        # Matching the hashed entered password to the stored hashed password
        if passw == verify_password:
            return True
        return False

    def allAcc(self):

        self.users.execute("SELECT * FROM users")

        data = self.users.fetchall()

        return data

    def get_acc(self):

        self.users.execute("SELECT * FROM users")

        data = self.users.fetchone()

        return data
