from backend.services.risk_service import (
    risk_service
)


class ReportService:

    def generate_summary(
        self,
        face_score,
        voice_score,
        writing_score
    ):

        report = (
            risk_service
            .generate_risk_report(
                face_score,
                voice_score,
                writing_score
            )
        )

        return {
            "summary":
                "Identity threat assessment completed.",
            **report
        }


report_service = ReportService()
