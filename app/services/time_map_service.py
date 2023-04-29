from typing import List, Optional
from datetime import datetime
from fastapi import Depends
from app.models.time_map_model import TimeMapModel
from app.repositories.time_map_repository import TimeMapRepository
from app.schemas.time_map_schema import TimeMapSchema, TimeMapKeyTimestampSchema, TimeMapValueSchema

class TimeMapService():

    def __init__(self, time_map_repository : TimeMapRepository = Depends()) -> None:
        self.time_map_repository : TimeMapRepository = time_map_repository

    def get(self, time_map_body : TimeMapKeyTimestampSchema) -> TimeMapModel:
        model = TimeMapModel(**time_map_body.dict())
        return self.time_map_repository.get(model)

    def exists(self, time_map_body : TimeMapKeyTimestampSchema) -> bool:
        model = self.get(time_map_body)
        if(model is None):
            return False
        return True

    def put(self, time_map_body: TimeMapSchema) -> TimeMapModel:
        model = TimeMapModel(**time_map_body.dict())
        return self.time_map_repository.put(model)

