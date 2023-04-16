import sqlite3


class Sqlite:
    def __init__(self):
        self.conn = sqlite3.connect('./db/gesture_recognition.db')
        self.cursor = self.conn.cursor()
        self.init_db()

    # init_db 初始化数据库
    def init_db(self):
        user_gesture = """
        CREATE TABLE IF NOT EXISTS t_user_gesture(
          f_id INTEGER PRIMARY KEY autoincrement NOT NULL ,
          f_name VARCHAR(16) NOT NULL,
          f_gestures VARCHAR(512) NOT NULL
        )
        """
        self.cursor.execute(user_gesture)
        user = """
                CREATE TABLE IF NOT EXISTS t_user(
                  f_id INTEGER PRIMARY KEY autoincrement NOT NULL ,
                  f_name VARCHAR(16) NOT NULL,
                  f_pwd VARCHAR(15) NOT NULL,
                  f_role_type varchar(5) NOT NULL
                )
                """
        self.cursor.execute(user)
        self.conn.commit()

    # release_conn 释放连接
    def release_conn(self):
        self.conn.close()

    def insert_data(self, data):
        sql = """
            INSERT INTO t_user_gesture (f_id, f_name, f_gestures)VALUES (?, ?, ?);
        """
        self.cursor.execute(sql, data)
        self.conn.commit()

    def get_data(self, name):
        sql = """
            SELECT f_id, f_name, f_gestures FROM t_user_gesture WHERE f_name = '%s';
        """
        self.cursor.execute(sql % name)
        res = self.cursor.fetchone()
        return res

    def update_data(self, data):
        sql = """
            UPDATE t_user_gesture SET f_name = ?, f_gestures = ? WHERE f_id = ?;
        """
        self.cursor.execute(sql, data)
        self.conn.commit()

    def get_user(self, name,role_type):
        sql = """
            SELECT f_id, f_name, f_pwd, f_role_type FROM t_user WHERE f_name = '%s' AND f_role_type = '%s';
        """
        self.cursor.execute(sql % (name,role_type))
        res = self.cursor.fetchone()
        return res
