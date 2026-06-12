from agents.identity_builder.prompts import (
    IDENTITY_BUILDER_PROMPT
)

from agents.identity_builder.tools import (
    build_identity_hash
)


class IdentityBuilderAgent:

    def __init__(self):

        self.name = (
            "IdentityBuilderAgent"
        )

    def run(
        self,
        user_data
    ):

        face_embedding = user_data.get(
            "face_embedding",
            []
        )

        voice_embedding = user_data.get(
            "voice_embedding",
            []
        )

        writing_embedding = user_data.get(
            "writing_embedding",
            []
        )

        identity_hash = (
            build_identity_hash(
                face_embedding,
                voice_embedding,
                writing_embedding
            )
        )

        return {
            "identity_hash":
                identity_hash,

            "confidence":
                95,

            "status":
                "EchoTwin Created"
        }
