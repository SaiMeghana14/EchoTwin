from pydantic import BaseModel


class EchoVisionRequest(BaseModel):

    linkedin_url: str | None = None

    github_url: str | None = None

    public_content: str | None = None


class EchoVisionResponse(BaseModel):

    face_clone_risk: str

    voice_clone_risk: str

    writing_clone_risk: str

    exposure_score: int

    recommendations: list[str]
