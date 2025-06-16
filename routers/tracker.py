from fastapi import APIRouter, Request
from db.database import SessionLocal
from models.click import Click

router = APIRouter()

@router.get("/click")
async def track_click(request: Request, source: str = None, campaign: str = None):
    db = SessionLocal()
    try:
        ip = request.client.host
        user_agent = request.headers.get("user-agent", "")
        referrer = request.headers.get("referer", "")

        click = Click(
            ip=ip,
            user_agent=user_agent,
            referrer=referrer,
            source=source,
            campaign=campaign
        )
        db.add(click)
        db.commit()
        return {"status": "ok"}
    finally:
        db.close()
