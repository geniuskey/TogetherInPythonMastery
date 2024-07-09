import mysql.connector

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='exampledb'
)

cur = conn.cursor()

# 데이터 삽입
cur.execute('''
INSERT INTO users (name, age) VALUES (%s, %s)
''', ('Alice', 30))

# 여러 데이터 삽입
users = [
    ('Bob', 25),
    ('Charlie', 35)
]
cur.executemany('''
INSERT INTO users (name, age) VALUES (%s, %s)
''', users)

# 변경 사항 저장
conn.commit()
conn.close()
