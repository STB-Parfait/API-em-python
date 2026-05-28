from fastapi import FastAPI
from datetime import date

app = FastAPI()


@app.get("/")
async def root(dia: date | None = None):

    if dia is None:
        dia = date.today()

    return {"dia": dia}