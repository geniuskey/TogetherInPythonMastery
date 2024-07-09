from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 설정
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 모델 정의
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)


# 테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 생성
db = SessionLocal()

try:
    # 데이터 삽입
    new_user = User(name='Alice', age=30)
    db.add(new_user)

    # 데이터베이스에 변경 사항 반영
    db.commit()
except:
    # 오류 발생 시 롤백
    db.rollback()
    raise
finally:
    # 세션 종료
    db.close()

# ----------------------------------------
# 컨텍스트 매니저를 사용한 트랜잭션 관리
from sqlalchemy.orm import Session

# 세션 생성 및 트랜잭션 관리
with Session(engine) as session:
    with session.begin():
        new_user = User(name='Bob', age=25)
        session.add(new_user)

# 예외 처리 및 트랜잭션 관리
try:
    with Session(engine) as session:
        with session.begin():
            another_user = User(name='Charlie', age=35)
            session.add(another_user)
except:
    print("Transaction failed and has been rolled back.")


# --------------------------------------------------
# 트랜잭션 예제
class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, index=True)
    balance = Column(Integer)


Base.metadata.create_all(bind=engine)


# --------------------------------------------------
# 트랜잭션을 사용한 송금 함수
def transfer_funds(session, from_account_id, to_account_id, amount):
    from_account = session.query(Account).filter(Account.id == from_account_id).one()
    to_account = session.query(Account).filter(Account.id == to_account_id).one()

    if from_account.balance < amount:
        raise ValueError("Insufficient funds")

    from_account.balance -= amount
    to_account.balance += amount


# 예제 실행
with Session(engine) as session:
    with session.begin():
        try:
            transfer_funds(session, from_account_id=1, to_account_id=2, amount=100)
        except ValueError as e:
            print(e)
            session.rollback()
