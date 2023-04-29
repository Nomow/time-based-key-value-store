from pydantic import BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):

    class Config:
        orm_mode = True

class TimeMapValueSchema(BaseSchema):

    value: str = Field(min_length=1)


class TimeMapKeyTimestampSchema(BaseSchema):

    key: str = Field(min_length=1)
    timestamp: datetime

class TimeMapSchema(TimeMapValueSchema, TimeMapKeyTimestampSchema):

    pass