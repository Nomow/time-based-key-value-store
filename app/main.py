import structlog
from fastapi import FastAPI
from app.configs.config import get_environment_variables
from app.middlewares.logger_middleware import RequestTimeLoggerMiddleware
from app.utils.db.database import init_db
from app.routers.time_map_router import TimeMapRouter
from app.utils.loggers.logger import config_structlog

config_structlog()
logger = structlog.get_logger()
logger.info('initializing application')

env = get_environment_variables()

app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
)

init_db()

app.include_router(TimeMapRouter)
app.add_middleware(RequestTimeLoggerMiddleware)

logger.info('application initialized')


