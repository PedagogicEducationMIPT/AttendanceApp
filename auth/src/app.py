from fastapi import FastAPI, HTTPException, Response, Header
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title='AttendanceApp',
    docs_url='/docs'
)

class RegistrationForm(BaseModel):
    username: str
    password: str

users: set[RegistrationForm] = set()

@app.post('/register')
def register(form: RegistrationForm):
    if form in users:
        raise HTTPException(
            status_code=400,
            detail='Уже зарегистрирован'
        ) 
    users.add(form)
    return Response(
        status_code=200,
        content='Успешно зарегистрирован.'
    )


@app.post('/auth')
def auth(form: RegistrationForm):
    if form not in users:
        raise HTTPException(
            status_code=400,
            detail='Нужно зарегистрироваться'
        )
    return hash(form.password)


private_info = 'Ответ: 10'

@app.get('/private/read')
def read(authorization: str = Header()):
    if hash(authorization) in [hash(user.password) for user in users]:
        return private_info
    else:
        raise HTTPException(
            status_code=400,
            detail='Нужно зарегистрироваться'
        )

uvicorn.run(app)