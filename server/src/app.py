from fastapi import FastAPI, Response, APIRouter
from src.db import AttendanceDatabase,Attendance


class WebApp(FastAPI):
    def __init__(self, db: AttendanceDatabase):
        super().__init__(title='AttendanceApp')
        self.db = db
        self.include_router(
            self.prepare_attendance_router()
        )

    def prepare_attendance_router(self):
        router = APIRouter(tags=['Attendance'],prefix='/attendance')
        @router.post('/record')
        def record(attendance: Attendance):
            self.db.record(attendance)
            return Response(status_code=200)

        @router.get('/info')
        def list_all_attendance():
            return self.db.list_all()
        
        return router
