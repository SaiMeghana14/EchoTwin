from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid


class ThreatBase(BaseModel):

    threat_type: str

    risk_score: float

    threat_level: str

    source: str


class ThreatCreate(ThreatBase):

    user_id: str

    evidence: Optional[str] = None


class ThreatResponse(ThreatBase):

    threat_id: str

    timestamp: datetime

    class Config:
        from_attributes = True


class Threat(ThreatBase):

    threat_id: str = Field(
        default_factory=lambda: str(uuid.uuid4())
    )

    user_id: str

    evidence: Optional[str] = None

    explanation: Optional[str] = None

    timestamp: datetime = Field(
        default_factory=datetime.utcnow
    )

    class Config:
        from_attributes = True
