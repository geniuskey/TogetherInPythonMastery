import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')
cur = conn.cursor()

# 데이터 업데이트
cur.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))

# 데이터 삭제
cur.execute('''
DELETE FROM users WHERE name = ?
''', ('Bob',))

# 변경 사항 저장
conn.commit()
conn.close()
