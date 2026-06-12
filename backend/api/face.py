from fastapi import APIRouter

from backend.schemas.face_analysis import (
    FaceAnalysisRequest,
    FaceAnalysisResponse
)

router = APIRouter(
    prefix="/face",
    tags=["Face Guardian"]
)


@router.post(
    "/analyze",
    response_model=FaceAnalysisResponse
)
async def analyze_face(
    payload: FaceAnalysisRequest
):

    # Replace later with DeepFace

    face_match = 91.5

    deepfake_probability = 72.4

    confidence = 89.3

    risk = (
        "HIGH"
        if deepfake_probability > 60
        else "LOW"
    )

    return FaceAnalysisResponse(
        face_match_score=face_match,
        deepfake_probability=deepfake_probability,
        confidence=confidence,
        risk_level=risk
    )
