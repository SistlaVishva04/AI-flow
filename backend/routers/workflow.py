from fastapi import APIRouter, UploadFile, File, Depends
import uuid
import fitz

from models.workflow_models import WorkflowRequest
from services.orchestrator import run_workflow
from utils.chunker import chunk_text
from services.vector_service import store_chunks
from services.workflow_service import save_workflow, list_workflows, get_workflow

from db.database import SessionLocal
from db.models import Document

from dependencies import get_current_user

router = APIRouter()

# ---------------- EXECUTE WORKFLOW ----------------
@router.post("/execute")
def execute_workflow(req: WorkflowRequest, user=Depends(get_current_user)):
    return run_workflow(req.nodes, req.edges, req.query)


# ---------------- UPLOAD PDF ----------------
@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    file_id = str(uuid.uuid4())

    content = await file.read()
    pdf = fitz.open(stream=content, filetype="pdf")

    text = ""
    for page in pdf:
        text += page.get_text()

    chunks = chunk_text(text, 500, 50)
    store_chunks(file_id, chunks)

    # Save metadata
    db = SessionLocal()
    doc = Document(
        id=file_id,
        filename=file.filename
    )
    db.add(doc)
    db.commit()
    db.close()

    return {
        "fileId": file_id,
        "fileName": file.filename,
        "chunksStored": len(chunks)
    }


# ---------------- SAVE WORKFLOW ----------------
@router.post("/save")
def save_workflow_api(payload: dict, user=Depends(get_current_user)):
    return save_workflow(
        user.id,        # 👈 Supabase user id
        payload["name"],
        payload["data"]
    )


# ---------------- LIST WORKFLOWS ----------------
@router.get("/list")
def list_workflow_api(user=Depends(get_current_user)):
    return list_workflows(user.id)


# ---------------- GET WORKFLOW ----------------
@router.get("/{wf_id}")
def get_workflow_api(wf_id: str, user=Depends(get_current_user)):
    return get_workflow(user.id, wf_id)
