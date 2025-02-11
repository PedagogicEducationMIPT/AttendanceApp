import pytest
from datetime import date
import pytest

from src.db import AttendanceDatabase, Attendance

@pytest.fixture
def records():
    return [
        Attendance(
            student_name='Sasha',
            date=date(year=2024,month=12,day=1)
        ),
        Attendance(
            student_name='Ivan',
            date=date(year=2024,month=12,day=1)
        ),
        Attendance(
            student_name='Ivan',
            date=date(year=2024,month=12,day=7)
        ),
    ]

@pytest.fixture
def database():
    database = AttendanceDatabase('test.json')
    yield database
    database.clear()