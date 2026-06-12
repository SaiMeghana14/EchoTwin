class RiskScoringEngine:

    def calculate_overall_risk(
        self,
        face_result=None,
        voice_result=None,
        writing_result=None
    ):

        face_risk = 0
        voice_risk = 0
        writing_risk = 0

        if face_result:
            face_risk = face_result.get(
                "deepfake_probability",
                0
            )

        if voice_result:
            voice_risk = voice_result.get(
                "clone_probability",
                0
            )

        if writing_result:
            writing_risk = writing_result.get(
                "impersonation_probability",
                0
            )

        overall = (
            face_risk * 0.4
            + voice_risk * 0.35
            + writing_risk * 0.25
        )

        return round(overall, 2)

    def determine_level(
        self,
        score
    ):

        if score >= 80:
            return "CRITICAL"

        if score >= 60:
            return "HIGH"

        if score >= 40:
            return "MEDIUM"

        return "LOW"

    def health_score(
        self,
        score
    ):
        return max(
            0,
            int(100 - score)
        )


risk_scoring_engine = (
    RiskScoringEngine()
)
