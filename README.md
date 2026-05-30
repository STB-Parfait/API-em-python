# Instruções de uso da API

### Iniciando a API:

##### Requisitos:

- Ter a linguagem Python instalada

##### Passo a passo:

1. Abra a pasta do projeto.
2. Digite `cmd` na barra de endereço.
3. Instale as dependências usando o comando `pip install -r requirements.txt`.
4. Rode o código usando o comando `python main.py`.

### Testando a API:
A forma mais simples de testar a API é usar a documentação gerada pelo swagger,
disponível em `http://localhost:8000/docs`.

Além disso, dentro dos arquivos do projeto há o arquivo `test_main.http`, nele está
listado dois testes simples, com e sem parâmetros para testar a rota da API.

Caso sua IDE não possua uma extenção para fazer requisições HTTP,
`HTTP Client` no caso do PyCharm ou `REST Client` no caso do VsCode, você
pode usar um app próprio, como o `Postman`, você pode enviar uma requisição
para as seguintes rotas:

##### Teste de rota SEM parâmetro:
`http://localhost:8000/`

##### Teste de rota COM parâmetro:
`http://localhost:8000/?dia=2000-01-01`  
*OBS:* O formato esperado para a data deve ser YYYY-MM-DD

##### Teste de rota com parâmetro inválido:
`http://localhost:8000/?dia=01-01-2000`