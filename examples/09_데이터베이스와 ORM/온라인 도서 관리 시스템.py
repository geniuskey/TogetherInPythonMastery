from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, timedelta, timezone

# 데이터베이스 설정
DATABASE_URL = 'sqlite:///library.db'  # SQLite 사용 시
# DATABASE_URL = 'mysql+mysqlconnector://user:password@localhost/librarydb'  # MySQL 사용 시

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# 모델 정의
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    available = Column(Integer, default=1)


class Rental(Base):
    __tablename__ = 'rentals'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    rented_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    returned_at = Column(DateTime, nullable=True)

    user = relationship("User")
    book = relationship("Book")


# 테이블 생성
Base.metadata.create_all(bind=engine)


# 사용자 및 도서 추가
def add_user(session, name, email):
    existing_user = session.query(User).filter(User.email == email).first()
    if existing_user:
        print(f"User with email {email} already exists.")
        return existing_user
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def add_book(session, title, author):
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


# 사용자 및 도서 조회
def get_users(session):
    return session.query(User).all()


def get_books(session):
    return session.query(Book).all()


# 예제 실행
with SessionLocal() as session:
    add_user(session, 'Alice', 'alice@example.com')
    add_user(session, 'Bob', 'bob@example.com')

    add_book(session, 'The Great Gatsby', 'F. Scott Fitzgerald')
    add_book(session, '1984', 'George Orwell')

    users = get_users(session)
    books = get_books(session)

    for user in users:
        print(user.name, user.email)

    for book in books:
        print(book.title, book.author, 'Available' if book.available else 'Not Available')


# 도서 대여
def rent_book(session, user_id, book_id):
    book = session.query(Book).filter(Book.id == book_id, Book.available == 1).first()
    if book:
        rental = Rental(user_id=user_id, book_id=book_id)
        book.available = 0
        session.add(rental)
        session.commit()
        return rental
    else:
        return None


# 도서 반납
def return_book(session, rental_id):
    rental = session.query(Rental).filter(Rental.id == rental_id, Rental.returned_at == None).first()
    if rental:
        rental.returned_at = datetime.now(timezone.utc)
        rental.book.available = 1
        session.commit()
        return rental
    else:
        return None


# 예제 실행
with SessionLocal() as session:
    try:
        rental = rent_book(session, user_id=1, book_id=1)
        if rental:
            print(f"Book rented: {rental.book.title} by {rental.user.name}")
        else:
            print("Book is not available for rent")

        returned_rental = return_book(session, rental.id)
        if returned_rental:
            print(f"Book returned: {returned_rental.book.title} by {returned_rental.user.name}")
        else:
            print("Rental not found or already returned")
    except Exception as e:
        session.rollback()
        print(f"Transaction failed: {e}")


def enforce_rental_period(session):
    overdue_rentals = session.query(Rental).filter(
        Rental.returned_at == None,
        Rental.rented_at < datetime.now(timezone.utc) - timedelta(days=30)
    ).all()

    for rental in overdue_rentals:
        rental.returned_at = datetime.now(timezone.utc)
        rental.book.available = 1

    if overdue_rentals:
        session.commit()
        for rental in overdue_rentals:
            print(f"Overdue book returned: {rental.book.title} by {rental.user.name}")


# 예제 실행
with SessionLocal() as session:
    enforce_rental_period(session)
