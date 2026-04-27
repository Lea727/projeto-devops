from fastapi import FastAPI
from pydantic import BaseModel

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define o modelo de dados para um Estudante usando Pydantic
class Estudante(BaseModel):
    nome: str
    curso: str

# Rota Raiz: Retorna uma mensagem de boas-vindas
@app.get("/")
def root():
    return {"message": "Sistema de Estudantes Online"}

# Rota de Cadastro: Recebe dados de um estudante e os retorna (simulando um salvamento)
@app.post("/estudantes/cadastro")
def create_estudante(estudante: Estudante):
    # Aqui o FastAPI valida automaticamente se os dados enviados estão corretos
    return estudante

# Rota de Saúde: Usada para monitorar se o servidor está rodando corretamente
@app.get("/saude")
def check_health():
    return {"status": "operacional"}