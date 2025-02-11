import pytest
from fastapi.testclient import TestClient
from src.app import WebApp
from pydantic import RootModel
from src.db import Attendance

@pytest.fixture
def app(database):
    app = WebApp(database)
    return TestClient(app)

class Attendances(RootModel):
    root: list[Attendance]

def test_record(app,records):
    record_request = app.post('/attendance/record',content=records[0].model_dump_json())
    assert record_request.status_code == 200
    list_request = app.get('/attendance')
    assert list_request.status_code == 200
    attendances = Attendances.model_validate_json(list_request.content) 
    assert attendances.root == [records[0]]