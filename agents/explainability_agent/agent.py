class ExplainabilityAgent:

    def __init__(self):

        self.name = (
            "ExplainabilityAgent"
        )

    def run(
        self,
        risk_result,
        face_result=None,
        voice_result=None,
        writing_result=None
    ):

        threat_level = risk_result.get(
            "threat_level"
        )

        overall_risk = risk_result.get(
            "overall_risk"
        )

        reasons = []

        if face_result:

            reasons.append(
                f"Face Deepfake Risk: "
                f"{face_result.get('deepfake_probability')}%"
            )

        if voice_result:

            reasons.append(
                f"Voice Clone Risk: "
                f"{voice_result.get('clone_probability')}%"
            )

        if writing_result:

            reasons.append(
                f"Writing Impersonation Risk: "
                f"{writing_result.get('impersonation_probability')}%"
            )

        return {

            "summary":
                f"Threat Level: "
                f"{threat_level}",

            "overall_risk":
                overall_risk,

            "evidence":
                reasons,

            "recommendation":
                "Review suspicious content and enable additional protections."
        }
