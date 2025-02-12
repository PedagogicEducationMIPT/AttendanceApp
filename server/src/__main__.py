import uvicorn
from src.app import WebApp
from src.db import AttendanceDatabase

app = WebApp(AttendanceDatabase('db.json'))

uvicorn.run(app)