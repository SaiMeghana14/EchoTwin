from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

from backend.schemas.upload import UploadResponse
from backend.config.folders import (
    FACE_UPLOADS,
    VOICE_UPLOADS,
    DOCUMENT_UPLOADS
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/face", response_model=UploadResponse)
async def upload_face(
    file: UploadFile = File(...)
):

    file_path = FACE_UPLOADS / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return UploadResponse(
        filename=file.filename,
        file_type="face",
        file_path=str(file_path),
        status="uploaded"
    )


@router.post("/voice", response_model=UploadResponse)
async def upload_voice(
    file: UploadFile = File(...)
):

    file_path = VOICE_UPLOADS / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return UploadResponse(
        filename=file.filename,
        file_type="voice",
        file_path=str(file_path),
        status="uploaded"
    )


@router.post("/document", response_model=UploadResponse)
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = DOCUMENT_UPLOADS / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return UploadResponse(
        filename=file.filename,
        file_type="document",
        file_path=str(file_path),
        status="uploaded"
    )
