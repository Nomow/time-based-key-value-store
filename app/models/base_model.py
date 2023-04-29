from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from app.utils.db.database import Base

class BaseModel(Base):

    __abstract__ = True
    created_at: DateTime = Column(DateTime, server_default=func.now())
    updated_at: DateTime = Column(DateTime, server_default=func.now(), onupdate=func.now())
