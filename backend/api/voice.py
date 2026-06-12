from fastapi import APIRouter

from backend.schemas.voice_analysis import (
    VoiceAnalysisRequest,
    VoiceAnalysisResponse
)

router = APIRouter(
    prefix="/voice",
    tags=["Voice Guardian"]
)


@router.post(
    "/analyze",
    response_model=VoiceAnalysisResponse
)
async def analyze_voice(
    payload: VoiceAnalysisRequest
):

    # Replace later with SpeechBrain

    voice_match = 86.1

    clone_probability = 69.7

    confidence = 92.4

    risk = (
        "HIGH"
        if clone_probability > 60
        else "LOW"
    )

    return VoiceAnalysisResponse(
        voice_match_score=voice_match,
        clone_probability=clone_probability,
        confidence=confidence,
        risk_level=risk
    )
