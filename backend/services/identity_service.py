import uuid

from backend.services.embedding_service import (
    embedding_service
)


class IdentityService:

    def create_identity_fingerprint(
        self,
        face_embedding,
        voice_embedding,
        writing_embedding
    ):

        identity_hash = (
            embedding_service
            .generate_identity_hash(
                face_embedding,
                voice_embedding,
                writing_embedding
            )
        )

        return {
            "twin_id": str(
                uuid.uuid4()
            ),
            "identity_hash":
                identity_hash
        }


identity_service = IdentityService()
