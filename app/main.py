from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from dotenv import load_dotenv
load_dotenv()

from app.database import engine, Base
from app.routes import comment, user, auth, task
from app.schemas.root import Root
from app.config import settings

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    debug=settings.debug if hasattr(settings, "debug") else False
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(comment.router)
app.include_router(task.router)

# Only mount static files if we are not on the API subdomain
@app.get("/")
async def get_root(request: Request):
    host = request.headers.get("host", "")
    if "api." in host:
        return JSONResponse({"status": "alive", "message": "LMI API is running. Use /docs for documentation."})
    return FileResponse("static/index.html")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/apps/{app_name}/")
async def get_app_file(app_name: str, request: Request):
    host = request.headers.get("host", "")
    if "api." in host:
         return JSONResponse({"error": "Not Found"}, status_code=404)
    
    file_path = f"static/apps/{app_name}/index.html"
    return FileResponse(file_path)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
