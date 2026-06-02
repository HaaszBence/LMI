from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from app.database import engine, Base
from app.routes import comment, user

from app.schemas.root import Root

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LetsMakeIt",
    description="Full-stack project."
)

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


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
