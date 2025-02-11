from datetime import date

from fastapi import FastAPI, Response
from src.db import AttendanceDatabase,Attendance


class WebApp(FastAPI):
    def __init__(self, db: AttendanceDatabase):
        super().__init__()
        self.db = db
        self.register()

    def register(self):
        @self.post('/attendance/record')
        def record(attendance: Attendance):
            self.db.record(attendance)
            return Response(status_code=200)

        @self.get('/attendance')
        def list_all_attendance():
            return self.db.list_all()


