from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid


class FaceSignature(BaseModel):
    embedding: List[float]
    confidence: float


class VoiceSignature(BaseModel):
    embedding: List[float]
    confidence: float


class WritingSignature(BaseModel):
    embedding: List[float]
    confidence: float


class IdentityFingerprint(BaseModel):

    face_signature: FaceSignature

    voice_signature: VoiceSignature

    writing_signature: WritingSignature

    identity_hash: str

    created_at: datetime


class IdentityCreate(BaseModel):

    user_id: str

    face_signature: Optional[FaceSignature] = None

    voice_signature: Optional[VoiceSignature] = None

    writing_signature: Optional[WritingSignature] = None


class IdentityResponse(BaseModel):

    twin_id: str

    user_id: str

    identity_hash: str

    health_score: int

    created_at: datetime


class EchoTwin(BaseModel):

    twin_id: str = Field(
        default_factory=lambda: str(uuid.uuid4())
    )

    user_id: str

    face_signature: Optional[FaceSignature] = None

    voice_signature: Optional[VoiceSignature] = None

    writing_signature: Optional[WritingSignature] = None

    identity_hash: str

    health_score: int = 100

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )

    class Config:
        from_attributes = True
