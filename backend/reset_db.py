import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)

# Drop the existing table and recreate it
metadata = MetaData()
metadata.reflect(bind=engine)

if 'users' in metadata.tables:
    print("Dropping existing users table...")
    users_table = Table('users', metadata, autoload_with=engine)
    users_table.drop(engine)

# Create the updated model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

print("Database reset and schema updated successfully!")