import random


class FaceDetector:

    def analyze(
        self,
        image_path: str
    ):

        return {
            "face_match_score":
                round(
                    random.uniform(
                        70,
                        98
                    ),
                    2
                ),

            "deepfake_probability":
                round(
                    random.uniform(
                        20,
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


face_detector = FaceDetector()
