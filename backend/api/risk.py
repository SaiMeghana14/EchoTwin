from fastapi import APIRouter

from backend.schemas.risk import (
    RiskRequest,
    RiskResponse
)

from backend.services.risk_service import (
    risk_service
)

router = APIRouter(
    prefix="/risk",
    tags=["Risk Intelligence"]
)


@router.post(
    "/calculate",
    response_model=RiskResponse
)
async def calculate_risk(
    payload: RiskRequest
):

    report = (
        risk_service
        .generate_risk_report(
            payload.face_risk,
            payload.voice_risk,
            payload.writing_risk
        )
    )

    return RiskResponse(
        overall_risk=report["overall_risk"],
        threat_level=report["threat_level"],
        health_score=report["health_score"]
    )
