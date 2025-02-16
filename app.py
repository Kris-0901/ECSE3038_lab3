from fastapi import FastAPI, Response, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError
from uuid import UUID, uuid4

app= FastAPI()

data=[]

class Tank(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    location:str
    lat:float
    lon:float

class Tank_Update(BaseModel):
    location:str | None = None
    lat:float | None = None
    lon:float | None = None

    @app.get("/tank")
    async def get_all_tanks():
        return data
