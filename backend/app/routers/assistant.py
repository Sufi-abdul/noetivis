
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from app.auth.deps import current_user
from app.security.consent import require_scopes
from app.security.audit_enforce import audit_request

router = APIRouter(prefix="/assistant", tags=["assistant"])

class AssistBody(BaseModel):
    task: str
    text: str

@router.post("/run")
def run(body: AssistBody, request: Request, user=Depends(current_user)):
    require_scopes(user, ["assistant:run"])
    # Stub: in production, call internal model/service using ONLY authorized data.
    audit_request(request, actor=user.get("sub","user"), action="assistant.run", resource="assistant", meta={"task": body.task})
    if body.task == "summarize":
        out = (body.text[:240] + "...") if len(body.text) > 240 else body.text
        return {"ok": True, "summary": out}
    if body.task == "tag":
        # naive tags
        tags = []
        t = body.text.lower()
        for k in ["invoice","royalty","partner","tax","payment","video","music"]:
            if k in t: tags.append(k)
        return {"ok": True, "tags": sorted(set(tags))}
    return {"ok": True, "result": "task stub executed"}
