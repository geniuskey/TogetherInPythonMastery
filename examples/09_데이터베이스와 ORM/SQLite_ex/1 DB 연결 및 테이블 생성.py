import sqlite3

# 데이터베이스 연결 (파일 기반)
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor()

# 테이블 생성
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

# 변경 사항 저장
conn.commit()

# 연결 종료
conn.close()
