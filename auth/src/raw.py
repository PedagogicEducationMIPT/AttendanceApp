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

users: set[str] = set()

@app.post('/public/register')
def register(form: RegistrationForm):
    json_dump = form.model_dump_json()
    if json_dump in users:
        raise HTTPException(
            status_code=400,
            detail='Уже зарегистрирован'
        ) 
    users.add(json_dump)
    return Response(
        status_code=200,
        content='Успешно зарегистрирован.'
    )


@app.post('/public/auth')
def auth(form: RegistrationForm):
    json_dump = form.model_dump_json()
    if json_dump not in users:
        raise HTTPException(
            status_code=400,
            detail='Нужно зарегистрироваться'
        )
    return json_dump


private_info = 'Ответ: 10'

class AuthorizationModel(BaseModel):
    token: str

@app.post('/private/read')
def read(authorization: AuthorizationModel):
    if authorization.token in users:
        return private_info
    else:
        raise HTTPException(
            status_code=400,
            detail='Нужно зарегистрироваться'
        )

uvicorn.run(app)