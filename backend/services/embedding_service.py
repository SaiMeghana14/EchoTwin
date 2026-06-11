import hashlib
import numpy as np


class EmbeddingService:

    def generate_identity_hash(
        self,
        face_embedding,
        voice_embedding,
        writing_embedding
    ):

        combined = (
            str(face_embedding)
            + str(voice_embedding)
            + str(writing_embedding)
        )

        return hashlib.sha256(
            combined.encode()
        ).hexdigest()

    def cosine_similarity(
        self,
        embedding_1,
        embedding_2
    ):

        embedding_1 = np.array(
            embedding_1
        )

        embedding_2 = np.array(
            embedding_2
        )

        similarity = np.dot(
            embedding_1,
            embedding_2
        ) / (
            np.linalg.norm(embedding_1)
            * np.linalg.norm(embedding_2)
        )

        return float(similarity)

    def compare_embeddings(
        self,
        stored_embedding,
        incoming_embedding
    ):

        similarity = self.cosine_similarity(
            stored_embedding,
            incoming_embedding
        )

        return {
            "similarity": round(
                similarity * 100,
                2
            )
        }


embedding_service = EmbeddingService()
