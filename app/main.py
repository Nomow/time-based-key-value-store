from fastapi import FastAPI
from app.configs.config import get_environment_variables
from app.utils.db.database import init_db
from app.routers.time_map_router import TimeMapRouter

env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)

init_db()
app.include_router(TimeMapRouter)