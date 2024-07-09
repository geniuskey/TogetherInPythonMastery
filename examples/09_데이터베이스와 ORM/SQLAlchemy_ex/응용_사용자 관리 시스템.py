from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

Base.metadata.create_all(bind=engine)

class UserManager:
    def __init__(self):
        self.db = SessionLocal()

    def add_user(self, name, age):
        new_user = User(name=name, age=age)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_user(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def update_user(self, user_id, name, age):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.age = age
            self.db.commit()
            return user
        return None

    def delete_user(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

    def list_users(self):
        return self.db.query(User).all()

    def close(self):
        self.db.close()

# 예제 실행
manager = UserManager()
manager.add_user('Alice', 30)
manager.add_user('Bob', 25)
for user in manager.list_users():
    print(user.name, user.age)
manager.update_user(1, 'Alice', 31)
print(manager.get_user(1).name, manager.get_user(1).age)
manager.delete_user(2)
for user in manager.list_users():
    print(user.name, user.age)
manager.close()
