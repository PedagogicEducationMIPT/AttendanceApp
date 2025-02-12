from fastapi import APIRouter, Response
from src.db import AttendanceDatabase,Attendance

class Handler:
    def __init__(self, db: AttendanceDatabase):
        self.db = db

    def record(self,attendance: Attendance):
        self.db.record(attendance)
        return Response(status_code=200)

    def list_all_attendance(self):
        return self.db.list_all()
    

class Router(APIRouter):
    def __init__(self, handler:Handler):
        super().__init__(tags='Attendance',prefix='/attendance')
        self.get('/record')(
            handler.record
        )
        self.post('/info')(
            handler.list_all_attendance
        )
     