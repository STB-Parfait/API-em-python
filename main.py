from fastapi import FastAPI
from datetime import date
import requests

app = FastAPI()


@app.get("/")
async def root(dia: date | None = None):

    if dia is None:
        dia = date.today()

    request_externa = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

    return {request_externa.status_code}