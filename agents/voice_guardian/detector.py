import random


class VoiceDetector:

    def analyze(
        self,
        audio_path
    ):

        return {

            "voice_match_score":
                round(
                    random.uniform(
                        65,
                        98
                    ),
                    2
                ),

            "clone_probability":
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


voice_detector = VoiceDetector()
