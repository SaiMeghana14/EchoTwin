from agents.voice_guardian.detector import (
    voice_detector
)


class VoiceGuardianAgent:

    def __init__(self):

        self.name = (
            "VoiceGuardianAgent"
        )

    def run(
        self,
        audio_path
    ):

        result = (
            voice_detector.analyze(
                audio_path
            )
        )

        probability = result[
            "clone_probability"
        ]

        if probability >= 80:
            risk = "CRITICAL"

        elif probability >= 60:
            risk = "HIGH"

        elif probability >= 40:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        return {
            **result,
            "risk_level": risk
        }
