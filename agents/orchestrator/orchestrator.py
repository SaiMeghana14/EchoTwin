from agents.identity_builder.agent import IdentityBuilderAgent
from agents.face_guardian.agent import FaceGuardianAgent
from agents.voice_guardian.agent import VoiceGuardianAgent
from agents.writing_guardian.agent import WritingGuardianAgent
from agents.risk_agent.agent import RiskAgent
from agents.explainability_agent.agent import ExplainabilityAgent


class EchoTwinOrchestrator:

    def __init__(self):

        self.identity_builder = IdentityBuilderAgent()

        self.face_guardian = FaceGuardianAgent()

        self.voice_guardian = VoiceGuardianAgent()

        self.writing_guardian = WritingGuardianAgent()

        self.risk_agent = RiskAgent()

        self.explainability_agent = ExplainabilityAgent()

    async def create_twin(
        self,
        user_data
    ):

        return self.identity_builder.run(
            user_data
        )

    async def analyze_content(
        self,
        image_path=None,
        audio_path=None,
        text=None
    ):

        face_result = None
        voice_result = None
        writing_result = None

        if image_path:

            face_result = (
                self.face_guardian.run(
                    image_path
                )
            )

        if audio_path:

            voice_result = (
                self.voice_guardian.run(
                    audio_path
                )
            )

        if text:

            writing_result = (
                self.writing_guardian.run(
                    text
                )
            )

        risk_result = (
            self.risk_agent.run(
                face_result,
                voice_result,
                writing_result
            )
        )

        explanation = (
            self.explainability_agent.run(
                risk_result,
                face_result,
                voice_result,
                writing_result
            )
        )

        return {
            "face": face_result,
            "voice": voice_result,
            "writing": writing_result,
            "risk": risk_result,
            "explanation": explanation
        }
