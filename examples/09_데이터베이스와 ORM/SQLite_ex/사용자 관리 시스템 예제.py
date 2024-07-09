import sqlite3

class UserManager:
    def __init__(self, db_name='example.db'):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
        ''')

    def add_user(self, name, age):
        self.cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
        ''', (name, age))
        self.conn.commit()

    def get_user(self, user_id):
        self.cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return self.cur.fetchone()

    def update_user(self, user_id, name, age):
        self.cur.execute('''
        UPDATE users SET name = ?, age = ? WHERE id = ?
        ''', (name, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()

    def list_users(self):
        self.cur.execute('SELECT * FROM users')
        return self.cur.fetchall()

    def close(self):
        self.conn.close()

# 예제 실행
manager = UserManager()
manager.add_user('Alice', 30)
manager.add_user('Bob', 25)
print(manager.list_users())
manager.update_user(1, 'Alice', 31)
print(manager.get_user(1))
manager.delete_user(2)
print(manager.list_users())
manager.close()
