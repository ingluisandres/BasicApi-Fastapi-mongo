import sys
sys.path.append("..")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import athletes, login, user


app = FastAPI(
    title="Juegos Olimpicos de 2020 en Japon",
    description="Datos de los Entrenadores, Deportistas, Medallas y los Equipos",
    version="0.1.0"
)

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(athletes.router)
app.include_router(user.router)
app.include_router(login.router)