from fastapi.testclient import TestClient
from app.main import app
def test_health():
    r=TestClient(app).get("/health"); assert r.status_code==200 and r.json()["status"]=="ok"
def test_blank_question_rejected(): assert TestClient(app).post("/ask",json={"question":"   "}).status_code==422
