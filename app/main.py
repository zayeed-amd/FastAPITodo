import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from .routers import auth as auth_router
from .routers import todos as todos_router

load_dotenv()

app = FastAPI(title="Todo API", version="1.0.0")

# CORS
origins = os.getenv("CORS_ORIGINS", "*")
allow_origins = [o.strip() for o in origins.split(",")] if origins else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Welcome to the FastAPI Todo API"}

# Routers
app.include_router(auth_router.router)
app.include_router(todos_router.router)
