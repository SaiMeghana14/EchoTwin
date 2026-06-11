from openai import AzureOpenAI

from backend.config.settings import settings


class ExplainabilityService:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            api_version="2024-02-15-preview",
            azure_endpoint=settings.azure_openai_endpoint
        )

    def explain_threat(
        self,
        face_score,
        voice_score,
        writing_score,
        threat_level
    ):

        prompt = f"""
You are the Explainability Agent of EchoTwin.

Face Risk: {face_score}
Voice Risk: {voice_score}
Writing Risk: {writing_score}

Threat Level:
{threat_level}

Explain:

1. Why content was flagged
2. Evidence used
3. User actions to take

Maximum 150 words.
"""

        response = self.client.chat.completions.create(
            model=settings.azure_openai_deployment,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


explainability_service = ExplainabilityService()
