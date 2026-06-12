from backend.services.embedding_service import (
    embedding_service
)


def build_identity_hash(
    face_embedding,
    voice_embedding,
    writing_embedding
):

    return (
        embedding_service
        .generate_identity_hash(
            face_embedding,
            voice_embedding,
            writing_embedding
        )
    )
