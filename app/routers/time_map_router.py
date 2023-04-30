from fastapi import HTTPException
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from app.schemas.time_map_schema import TimeMapSchema, TimeMapValueSchema, TimeMapKeyTimestampSchema, BaseSchema
from app.services.time_map_service import TimeMapService

TimeMapRouter = APIRouter(tags=["TimeMap"])

@TimeMapRouter.get("/", response_model=TimeMapValueSchema)
async def get(time_map_body : TimeMapKeyTimestampSchema, time_map_service : TimeMapService = Depends()):
    model = time_map_service.get(time_map_body)
    if(model is None):
        raise HTTPException(status_code=404, detail="Time Map not found")
    return model

@TimeMapRouter.put("/", response_model=BaseSchema)
async def put(time_map_body : TimeMapSchema, time_map_service : TimeMapService = Depends()):
    if(time_map_service.exists(time_map_body) == False):
        time_map_service.put(time_map_body)
        return JSONResponse(content = {}, status_code=201)
    return time_map_service.put(time_map_body)




