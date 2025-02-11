from datetime import date

from fastapi import FastAPI, Response
from pydantic import BaseModel
from src.db import AttendanceDatabase

app = FastAPI('/')
db = 




@app.post('/attendance/record')
def record():
    return Response(status_code=200)

@app.get('/attendance')
def list_all_attendance():
