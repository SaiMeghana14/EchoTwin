from fastapi import APIRouter

from backend.schemas.identity import (
    IdentityCreate,
    IdentityResponse
)

from backend.services.identity_service import (
    identity_service
)

router = APIRouter(
    prefix="/identity",
    tags=["Identity"]
)


@router.post(
    "/create",
    response_model=IdentityResponse
)
async def create_identity(
    payload: IdentityCreate
):

    fingerprint = (
        identity_service
        .create_identity_fingerprint(
            payload.face_signature.embedding
            if payload.face_signature else [],

            payload.voice_signature.embedding
            if payload.voice_signature else [],

            payload.writing_signature.embedding
            if payload.writing_signature else []
        )
    )

    return IdentityResponse(
        twin_id=fingerprint["twin_id"],
        user_id=payload.user_id,
        identity_hash=fingerprint["identity_hash"],
        health_score=100,
        created_at=None
    )
