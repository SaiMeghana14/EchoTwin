from agents.writing_guardian.stylometry import (
    stylometry_engine
)


class WritingGuardianAgent:

    def __init__(self):

        self.name = (
            "WritingGuardianAgent"
        )

    def run(
        self,
        text
    ):

        result = (
            stylometry_engine.analyze(
                text
            )
        )

        probability = result[
            "impersonation_probability"
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
