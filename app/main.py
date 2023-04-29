from fastapi import FastAPI
from app.utils.db.database import init_db
from app.routers.time_map_router import TimeMapRouter

init_db()
app = FastAPI()
app.include_router(TimeMapRouter)