from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.upload import router as upload_router
from backend.api.identity import router as identity_router
from backend.api.face import router as face_router
from backend.api.voice import router as voice_router
from backend.api.writing import router as writing_router
from backend.api.risk import router as risk_router
from backend.api.echovision import router as echovision_router

from backend.config.settings import settings

app = FastAPI(
    title="EchoTwin API",
    description="AI Identity Guardian Platform",
    version="1.0.0"
)

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes

app.include_router(upload_router)
app.include_router(identity_router)
app.include_router(face_router)
app.include_router(voice_router)
app.include_router(writing_router)
app.include_router(risk_router)
app.include_router(echovision_router)


@app.get("/")
async def root():
    return {
        "project": "EchoTwin",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment
    }
