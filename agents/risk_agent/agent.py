from agents.risk_agent.scoring import (
    risk_scoring_engine
)


class RiskAgent:

    def __init__(self):

        self.name = "RiskAgent"

    def run(
        self,
        face_result=None,
        voice_result=None,
        writing_result=None
    ):

        overall = (
            risk_scoring_engine
            .calculate_overall_risk(
                face_result,
                voice_result,
                writing_result
            )
        )

        return {

            "overall_risk":
                overall,

            "threat_level":
                risk_scoring_engine
                .determine_level(
                    overall
                ),

            "health_score":
                risk_scoring_engine
                .health_score(
                    overall
                )
        }
