from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------
# 데이터베이스 연결 설정
DATABASE_URL = 'sqlite:///example.db'  # SQLite 사용 시
# DATABASE_URL = 'mysql+mysqlconnector://user:password@localhost/exampledb'  # MySQL 사용 시

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ---------------------------------------------------
# 데이터 모델 정의
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)


# ---------------------------------------------------
# 데이터베이스 연동
from sqlalchemy.orm import Session

# 세션 생성
db = SessionLocal()

# 새로운 사용자 객체 생성
new_user = User(name='Alice', age=30)

# 데이터베이스에 사용자 추가
db.add(new_user)
db.commit()
db.refresh(new_user)

print(new_user.id)  # 새로운 사용자 ID 출력

# 세션 종료
db.close()


# ---------------------------------------------------
# 데이터 조회
# 세션 생성
db = SessionLocal()

# 사용자 조회
users = db.query(User).all()
for user in users:
    print(user.name, user.age)

# 사용자 ID로 조회
user = db.query(User).filter(User.id == 1).first()
print(user.name, user.age)

# 세션 종료
db.close()


# ---------------------------------------------------
# 데이터 업데이트 및 삭제
# 세션 생성
db = SessionLocal()

# 사용자 업데이트
user = db.query(User).filter(User.id == 1).first()
user.age = 31
db.commit()

# 사용자 삭제
user = db.query(User).filter(User.id == 1).first()
db.delete(user)
db.commit()

# 세션 종료
db.close()
