import uvicorn
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Get the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Mount static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Initialize templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/")
async def home(request: Request):
    """
    Render the home page with resume alignment form
    """
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/profile")
async def profile(request: Request):
    """
    Render the profile setup page
    """
    return templates.TemplateResponse("profile.html", {"request": request})

@app.post("/align")
async def align_resume(
    request: Request,
    resume_file: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Handle resume alignment
    """
    # TODO: Implement resume alignment logic
    return {"message": "Resume alignment not implemented yet"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8090, reload=True)