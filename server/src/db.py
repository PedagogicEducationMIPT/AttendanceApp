import json
from datetime import date
from pathlib import Path
from pydantic import BaseModel

class Attendance(BaseModel):
    date: date
    student_name: str

class DataBaseModel(BaseModel):
    attendances: list[Attendance]    

class AttendanceDatabase:
    def __init__(self,file_name: str):
        self.file_path = Path(file_name)
        self._initialize_database()
        
    def _initialize_database(self):
        self.file_path.touch()
        with self.file_path.open('w') as f:
            f.write(DataBaseModel(attendances=[]).model_dump_json())
        
    def _retrieve_rows(self) -> DataBaseModel:
        with self.file_path.open('r') as f:
            return DataBaseModel.model_validate_json(f.read())
        
    def list_all(self):
        return self._retrieve_rows().attendances

    def record(self, attendance: Attendance):
        db = self._retrieve_rows()
        db.attendances.append(attendance)
        with self.file_path.open('w') as f:
            f.write(db.model_dump_json())

    def clear(self):
        self.file_path.unlink()

