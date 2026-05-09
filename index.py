from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from docxtpl import DocxTemplate
from pathlib import Path
import uuid

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

# Ton template est à la racine du repo GitHub
TEMPLATE_PATH = BASE_DIR / "template_pfe_encg_original_mise_en_page.docx"


@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "PFE DOCX API is running",
        "template_exists": TEMPLATE_PATH.exists()
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "template_exists": TEMPLATE_PATH.exists()
    }


@app.post("/fill-pfe")
async def fill_pfe(request: Request):
    try:
        payload = await request.json()

        if not TEMPLATE_PATH.exists():
            return JSONResponse(
                status_code=404,
                content={
                    "error": "Template Word introuvable",
                    "expected_path": str(TEMPLATE_PATH)
                }
            )

        context = payload.get("data", payload)

        doc = DocxTemplate(str(TEMPLATE_PATH))

        filename = f"rapport_pfe_encg_{uuid.uuid4().hex[:8]}.docx"
        output_path = Path("/tmp") / filename

        doc.render(context)
        doc.save(output_path)

        return FileResponse(
            path=str(output_path),
            filename=filename,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
