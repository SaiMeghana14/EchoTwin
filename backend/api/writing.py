from fastapi import APIRouter

from backend.schemas.writing_analysis import (
    WritingAnalysisRequest,
    WritingAnalysisResponse
)

router = APIRouter(
    prefix="/writing",
    tags=["Writing Guardian"]
)


@router.post(
    "/analyze",
    response_model=WritingAnalysisResponse
)
async def analyze_writing(
    payload: WritingAnalysisRequest
):

    # Replace later with stylometry

    similarity = 78.4

    impersonation_probability = 63.2

    confidence = 84.5

    risk = (
        "HIGH"
        if impersonation_probability > 60
        else "LOW"
    )

    return WritingAnalysisResponse(
        writing_similarity=similarity,
        impersonation_probability=impersonation_probability,
        confidence=confidence,
        risk_level=risk
    )
