from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext
import uvicorn

app = FastAPI()

# Initialize Passlib CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Hash the password (this should be done once and stored securely)
hashed_password = pwd_context.hash(input())

# Define the API key header
api_key_header = APIKeyHeader(name="X-API-Key")

# Dependency to check the API key securely
def check_api_key(api_key: str = Depends(api_key_header)):
    if not pwd_context.verify(api_key, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API Key",
        )
    return api_key

# Protected endpoint
@app.get("/protected")
def protected_route(api_key: str = Depends(check_api_key)):
    return {"message": "Access granted", "api_key": api_key}

# Unprotected endpoint
@app.get("/unprotected")
def unprotected_route():
    return {"message": "This is a public endpoint"}


uvicorn.run(app)