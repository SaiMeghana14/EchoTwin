from datetime import datetime
import uuid


class ThreatService:

    def build_threat_record(
        self,
        threat_type,
        risk_score,
        threat_level,
        explanation=None
    ):

        return {
            "threat_id":
                str(uuid.uuid4()),

            "threat_type":
                threat_type,

            "risk_score":
                risk_score,

            "threat_level":
                threat_level,

            "explanation":
                explanation,

            "timestamp":
                datetime.utcnow().isoformat()
        }


threat_service = ThreatService()
