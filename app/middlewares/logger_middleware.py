import time
import structlog
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestTimeLoggerMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        logger = structlog.get_logger()
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        logger.info('request processing time in (s): ', request_time=process_time)
        return response
