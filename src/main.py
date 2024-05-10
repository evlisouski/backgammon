from fastapi import FastAPI
from src.score.router import router as router_score

app = FastAPI()

app.include_router(router_score)


@app.get("/health_check", tags=["health_check"])
def health_check():
    return "OK"
