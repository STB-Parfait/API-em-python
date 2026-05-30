from typing import Annotated
from fastapi import FastAPI, Request, Query
from datetime import date
import requests
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

class ApiResponse(BaseModel):
    data: date
    conteudo: object
    mensagem: str

class InvalidParameterException(BaseModel):
    mensagem: str

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"mensagem": "Parâmetro usado é inválido ou não está no formato YYYY-MM-DD"}
    )

@app.get(
    "/",
    tags=["Rotas"],
    response_description="Dia enviado como parâmetro (ou o dia de hoje) + Lista Recebida da API externa",
    response_model=ApiResponse,
    responses={
        422: {"model": InvalidParameterException, "description": "Invalid parameter provided"},
    },
)
async def root(
        dia: Annotated[
            date | None,
            Query(
                alias="data",
                description="Data no formato YYYY-MM-DD",
            )
        ] = None,
) -> ApiResponse:

    if dia is None:
        dia = date.today()

    request_externa = requests.get("https://testedefensoriapr.pythonanywhere.com/precos")

    if request_externa.status_code != 200:
        return ApiResponse(
            data=dia,
            conteudo="[]",
            mensagem="Não foi possível consumir a API externa :("
        )

    else:
        return ApiResponse(
            data=dia,
            conteudo=request_externa.json(),
            mensagem="API externa consumida com sucesso :)"
        )