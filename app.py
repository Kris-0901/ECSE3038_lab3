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
    long:float

class Tank_Update(BaseModel):
    location:str | None = None
    lat:float | None = None
    long:float | None = None

    @app.get("/tank")
    async def get_all_tanks():
        return data
    
    @app.post("/tank")
    async def add_tank(new_tank:Tank):

        if not new_tank.location:
            raise HTTPException(status_code=422,detail="Invalid request: 'location' filed missing ")
        
        if new_tank.lat is None or new_tank.lat is None: 
            raise HTTPException(status_code=422,detail="Invalid request: 'lat' or 'long' filed missing")
        
        tank_json= jsonable_encoder(new_tank)
        data.append(new_tank)
        return JSONResponse(tank_json,status_code=201)
        
