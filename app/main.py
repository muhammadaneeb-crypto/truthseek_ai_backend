from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .schemas import AskRequest, AskResponse, Source
from .agent import run_agent
app=FastAPI(title="TruthSeek AI API",version="1.0.0")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["GET","POST"],allow_headers=["Content-Type","X-API-Key"])
def authorize(key: str|None):
    if settings.app_api_key and key != settings.app_api_key: raise HTTPException(status_code=401,detail="Invalid or missing API key")
@app.get("/health")
def health(): return {"status":"ok","service":"TruthSeek AI","groq_configured":bool(settings.groq_api_key),"tavily_configured":bool(settings.tavily_api_key),"api_key_protection":bool(settings.app_api_key)}
async def execute(payload: AskRequest,key: str|None,force: bool):
    authorize(key)
    try:
        state=run_agent(payload.question,force_research=force or payload.use_web is True)
        sources=[Source(title=s["title"],url=s["url"],snippet=s.get("content","")[:400]) for s in state.get("search_results",[])]
        return AskResponse(answer=state.get("answer","No answer returned."),verification_status=state.get("verification_status","unverified"),used_web=state.get("used_web",False),sources=sources,uncertainty_notes=state.get("uncertainty_notes",[]))
    except HTTPException: raise
    except Exception as exc: raise HTTPException(status_code=502,detail=f"Agent request failed ({type(exc).__name__}).") from exc
@app.post("/ask",response_model=AskResponse)
async def ask(payload: AskRequest,x_api_key: str|None=Header(default=None)): return await execute(payload,x_api_key,False)
@app.post("/research",response_model=AskResponse)
async def research(payload: AskRequest,x_api_key: str|None=Header(default=None)): return await execute(payload,x_api_key,True)
