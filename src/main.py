from fastapi import FastAPI
from src.score.router import router as router_score

app = FastAPI()

app.include_router(router_score)


@app.get("/")
def get_main_page():
    return "The main page!"
