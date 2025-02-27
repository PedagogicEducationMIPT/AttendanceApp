import uvicorn
import fastapi

app = fastapi.FastAPI()

@app.get('/')
def hello():
    return 'hello'

uvicorn.run(
    app,
    ssl_certfile='certificate.crt',
    ssl_keyfile='private.key'
)