from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test123@127.0.0.1:5432/time_based_key_value_store2"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Initialized the db")
