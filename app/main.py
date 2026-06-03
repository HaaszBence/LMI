from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from dotenv import load_dotenv
load_dotenv()

from app.database import engine, Base
from app.routes import comment, user, auth
from app.schemas.root import Root

# ... (middle of file)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(comment.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root():
    return FileResponse("static/index.html")

@app.get("/apps/synapse/")
def get_synapse():
    return FileResponse("static/apps/synapse/index.html")

@app.get("/apps/tasker/")
def get_tasker():
    return FileResponse("static/apps/tasker/index.html")

@app.get("/apps/auth/")
def get_auth():
    return FileResponse("static/apps/auth/index.html")


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
