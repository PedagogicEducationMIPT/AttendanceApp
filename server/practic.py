from pathlib import Path
from datetime import date

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Attendance(BaseModel):
    name: str
    date: date

class AttendanceDatabaseModel(BaseModel):
    attendances: dict[str,bool]

file = 'db.json'
if not Path(file).exists():
    with open(file,'w') as f:
        f.write(AttendanceDatabaseModel(attendances={}).model_dump_json())

@app.post('/attendance/record')
def home(attendance: Attendance):
    with open(file,'r') as f:
        db = AttendanceDatabaseModel.model_validate_json(f.read())
    db.attendances[attendance.model_dump_json()] = True
    with open(file,'w') as f:
        f.write(db.model_dump_json())


# @app.get('/attendance/list')
# def home():
#     return serialize(attendances)

uvicorn.run(app,port=5000)
