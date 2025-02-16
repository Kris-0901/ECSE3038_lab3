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

@app.get("/tank{id}")
async def find_tank(id:UUID):
    for tank in data:
        if tank.id == id:
            tank_json=jsonable_encoder(tank)
            return JSONResponse(tank_json,status_code=200)
        raise HTTPException(status_code=404, detail="Tank not found")
    
@app.patch("/tank/{id}")
async def update_tank(id:UUID,updated_tank:Tank_Update):
    for i, tank in enumerate(data):
        if tank.id == id:
            tank_upadte_dict=updated_tank.model_dump(exclude_unset=True)

            try: 
                new_updated_tank=tank.copy(update=tank_upadte_dict)
                data[i]=Tank.model_validate(new_updated_tank)
                json_new_updated_tank=jsonable_encoder(new_updated_tank)
                return JSONResponse(json_new_updated_tank,status_code=200)
            except ValidationError:
                raise HTTPException(status_code=400, detail="Invalid Request: Tank should consist of a 'location', 'lat' or 'long'")
        raise HTTPException(status_code=400, detail="Tank not found")

        
