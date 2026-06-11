from pydantic import BaseModel


class RiskRequest(BaseModel):

    face_risk: float

    voice_risk: float

    writing_risk: float


class RiskResponse(BaseModel):

    overall_risk: float

    threat_level: str

    health_score: int
