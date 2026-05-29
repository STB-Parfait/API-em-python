from fastapi import FastAPI
from datetime import date
import requests

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

@app.get(
    "/",
    tags=["Rotas"],
    response_description="Dia enviado como parâmetro (ou o dia de hoje) + Lista Recebida da API externa",
)
async def root(dia: date | None = None):

    if dia is None:
        dia = date.today()

    request_externa = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

    if request_externa.status_code != 200:
        return {
            "data": dia,
            "mensagem": "Não foi possível consumir a API externa :("
        }
    else:
        return {
            "data": dia,
            "conteudo": request_externa.json(),
            "mensagem": "API externa consumida com sucesso :)"
        }