import structlog
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from app.configs.config import get_environment_variables

logger = structlog.get_logger()

env = get_environment_variables()

DATABASE_URL = f"{env.DATABASE_DIALECT}://{env.DATABASE_USERNAME}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOSTNAME}:{env.DATABASE_PORT}/{env.DATABASE_NAME}"

engine = create_engine(
    DATABASE_URL, echo=env.DEBUG_MODE, future=True
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()

def get_db_connection():
    db = scoped_session(SessionLocal)
    try:
        yield db
    finally:
        db.close()

def init_db():
    if not database_exists(engine.url):
        logger.info('database does not exists creating new database')
        create_database(engine.url)
    else:
        logger.info('database exists omitting creation of new database')
    Base.metadata.create_all(bind=engine)
