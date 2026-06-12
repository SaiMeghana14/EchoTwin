class TwinShieldAgent:

    def __init__(self):

        self.name = (
            "TwinShieldAgent"
        )

    def run(
        self,
        risk_data
    ):

        threat_level = risk_data.get(
            "threat_level",
            "LOW"
        )

        actions = []

        if threat_level == "CRITICAL":

            actions = [

                "Enable MFA immediately",

                "Remove sensitive public content",

                "Review account activity",

                "Monitor impersonation attempts",

                "Report malicious content"
            ]

        elif threat_level == "HIGH":

            actions = [

                "Enable MFA",

                "Reduce public exposure",

                "Monitor public mentions"
            ]

        elif threat_level == "MEDIUM":

            actions = [

                "Review privacy settings",

                "Audit public content"
            ]

        else:

            actions = [

                "Continue monitoring"
            ]

        return {

            "protection_level":
                threat_level,

            "recommended_actions":
                actions
        }
