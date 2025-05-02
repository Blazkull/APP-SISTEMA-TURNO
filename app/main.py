import os
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, Request
from core.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware  # habilitar CORS
from routers import roles


app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "API en línea en Render"}

#incluir los routers para su uso
app.include_router(roles.router)
    
# Configuración de CORS
origins = [
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://localhost:8080",
    "https://mi-dominio.com",
    "https://otro-dominio.net",
    "*",  # Solo para desarrollo
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


