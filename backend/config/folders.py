from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

UPLOAD_DIR = ROOT_DIR / "storage" / "uploads"

FACE_UPLOADS = UPLOAD_DIR / "faces"

VOICE_UPLOADS = UPLOAD_DIR / "voices"

DOCUMENT_UPLOADS = UPLOAD_DIR / "documents"

PROCESSED_DIR = ROOT_DIR / "storage" / "processed"

EMBEDDINGS_DIR = PROCESSED_DIR / "embeddings"

REPORTS_DIR = PROCESSED_DIR / "reports"

HEATMAPS_DIR = PROCESSED_DIR / "heatmaps"


def create_folders():

    folders = [
        FACE_UPLOADS,
        VOICE_UPLOADS,
        DOCUMENT_UPLOADS,
        EMBEDDINGS_DIR,
        REPORTS_DIR,
        HEATMAPS_DIR,
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
