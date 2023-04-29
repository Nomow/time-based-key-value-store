from fastapi import Depends
from sqlalchemy.orm import Session
from app.utils.db.database import get_db_connection
from app.models.time_map_model import TimeMapModel


class TimeMapRepository():

    def __init__(self, db : Session = Depends(get_db_connection)) -> None:
        self.db = db

    def get(self, time_map: TimeMapModel) -> TimeMapModel:
        return self.db.get(TimeMapModel, (time_map.timestamp, time_map.key))

    def create(self, time_map: TimeMapModel) -> TimeMapModel:
        self.db.add(time_map)
        self.db.commit()
        self.db.refresh(time_map)
        return time_map
    def put(self, time_map: TimeMapModel) -> TimeMapModel:
        self.db.merge(time_map)
        self.db.commit()
        return time_map

