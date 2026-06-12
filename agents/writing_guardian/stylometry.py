import random


class StylometryEngine:

    def analyze(
        self,
        text
    ):

        return {

            "writing_similarity":
                round(
                    random.uniform(
                        60,
                        98
                    ),
                    2
                ),

            "impersonation_probability":
                round(
                    random.uniform(
                        10,
                        90
                    ),
                    2
                ),

            "confidence":
                round(
                    random.uniform(
                        80,
                        99
                    ),
                    2
                )
        }


stylometry_engine = (
    StylometryEngine()
)
