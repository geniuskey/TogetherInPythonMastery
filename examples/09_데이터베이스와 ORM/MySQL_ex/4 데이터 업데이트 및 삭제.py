import mysql.connector

# 데이터베이스 연결
conn = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='exampledb'
)

cur = conn.cursor()

# 데이터 업데이트
cur.execute('''
UPDATE users SET age = %s WHERE name = %s
''', (31, 'Alice'))

# 데이터 삭제
cur.execute('''
DELETE FROM users WHERE name = %s
''', ('Bob',))

# 변경 사항 저장
conn.commit()
conn.close()
