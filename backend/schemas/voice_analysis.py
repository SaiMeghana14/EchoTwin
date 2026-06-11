from pydantic import BaseModel


class VoiceAnalysisRequest(BaseModel):

    audio_path: str

    user_id: str


class VoiceAnalysisResponse(BaseModel):

    voice_match_score: float

    clone_probability: float

    confidence: float

    risk_level: str
