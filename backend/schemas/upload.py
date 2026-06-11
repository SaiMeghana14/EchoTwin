from pydantic import BaseModel


class UploadResponse(BaseModel):

    filename: str

    file_type: str

    file_path: str

    status: str
