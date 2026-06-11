class RiskService:

    def calculate_overall_risk(
        self,
        face_risk,
        voice_risk,
        writing_risk
    ):

        overall = (
            face_risk * 0.4
            + voice_risk * 0.35
            + writing_risk * 0.25
        )

        return round(overall, 2)

    def threat_level(
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

    def identity_health_score(
        self,
        risk_score
    ):

        health = 100 - risk_score

        return max(
            0,
            int(health)
        )

    def generate_risk_report(
        self,
        face_risk,
        voice_risk,
        writing_risk
    ):

        overall = self.calculate_overall_risk(
            face_risk,
            voice_risk,
            writing_risk
        )

        return {
            "overall_risk": overall,
            "health_score":
                self.identity_health_score(
                    overall
                ),
            "threat_level":
                self.threat_level(
                    overall
                )
        }


risk_service = RiskService()
