from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from ..auth import verify_token

router = APIRouter(prefix="/files", tags=["Files"])

# Vercel allows temporary file storage in /tmp
UPLOAD_DIR = Path("/tmp/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".pdf", ".txt", ".csv"}
MAX_FILE_SIZE = 5 * 1024 * 1024


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    current_user: dict = Depends(verify_token),
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected")

    original_name = Path(file.filename).name
    extension = Path(original_name).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed")

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size must be less than 5 MB",
        )

    unique_filename = f"{uuid4()}{extension}"
    file_path = UPLOAD_DIR / unique_filename
    file_path.write_bytes(content)

    return {
        "message": "File uploaded successfully",
        "original_filename": original_name,
        "stored_filename": unique_filename,
        "uploaded_by": current_user.get("sub"),
        "file_size": len(content),
    }
