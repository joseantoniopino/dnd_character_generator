# database.py
import mysql.connector


class Database:
    def connect(self):
        raise NotImplementedError


class MySQLDatabase(Database):
    def connect(self):
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="greenwood",
            password="password",
            database="character_db"
        )
        return connection
