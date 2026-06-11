from pydantic import BaseModel


class FaceAnalysisRequest(BaseModel):

    image_path: str

    user_id: str


class FaceAnalysisResponse(BaseModel):

    face_match_score: float

    deepfake_probability: float

    confidence: float

    risk_level: str
