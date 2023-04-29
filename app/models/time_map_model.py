from sqlalchemy import Column, String, DateTime
from app.models.base_model import BaseModel

class TimeMapModel(BaseModel):

    __tablename__ = "TimeMap"
    timestamp : DateTime = Column(DateTime, primary_key=True, index=True)
    key : String = Column(String, primary_key=True, index=True)
    value : String = Column(String, default=False)