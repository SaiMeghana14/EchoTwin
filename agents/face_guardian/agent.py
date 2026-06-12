from agents.face_guardian.detector import (
    face_detector
)


class FaceGuardianAgent:

    def __init__(self):

        self.name = (
            "FaceGuardianAgent"
        )

    def run(
        self,
        image_path
    ):

        result = (
            face_detector.analyze(
                image_path
            )
        )

        probability = result[
            "deepfake_probability"
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
