from fastapi import FastAPI
from db.init import init_db
from routers.tracker import router as tracker_router

app = FastAPI()
init_db()
app.include_router(tracker_router)
