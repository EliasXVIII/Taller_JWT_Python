from fastapi import FastAPI
import time
from jose import jwt
from fastapi.staticfiles import StaticFiles
from os import getenv
from dotenv import load_dotenv

load_dotenv()
clave_secreta = getenv("clave_secreta")

app = FastAPI()

caducidad = int(time.time()) + 240 ###  + 240 
print(type(caducidad))
print(caducidad)

app.mount("/static", StaticFiles(directory="static"), name="static")

print("---------Token-------------")

token = jwt.encode({"id":"1", "nombre": "Elias", "time": caducidad}, key=clave_secreta, algorithm="HS256")

print(token)

print("---------Info-------------")

token_resuelto = jwt.decode(token, key=clave_secreta, algorithms=["HS256"])

print(token_resuelto)

@app.get("/token")
def get_token():
    return {"token": token}

def verificar_token(token):
    mensaje = jwt.decode(token, clave_secreta, algorithms=["HS256"])
    return mensaje

@app.post("/verificar/{token}")
def verificar_token_route(token: str):
    mensaje = verificar_token(token)
    return mensaje

## para visualizar el token en http://127.0.0.1:8000/static/index.html
    