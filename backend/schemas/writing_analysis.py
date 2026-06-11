from pydantic import BaseModel


class WritingAnalysisRequest(BaseModel):

    text: str

    user_id: str


class WritingAnalysisResponse(BaseModel):

    writing_similarity: float

    impersonation_probability: float

    confidence: float

    risk_level: str
