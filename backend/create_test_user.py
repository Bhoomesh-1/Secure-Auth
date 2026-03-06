import os
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import bcrypt

# Database setup
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_test_user():
    db = SessionLocal()
    try:
        # Check if user exists
        existing = db.query(User).filter(User.email == 'test@example.com').first()
        if existing:
            print("Test user already exists")
            return

        # Create test user
        hashed = hash_password('TestPass123!')
        test_user = User(
            username='Test User',
            email='test@example.com',
            password_hash=hashed
        )
        db.add(test_user)
        db.commit()
        print("Test user created successfully!")
        print("Email: test@example.com")
        print("Password: TestPass123!")

    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == '__main__':
    create_test_user()