from fastapi.testclient import TestClient
from src.main import app

# Cria um cliente de teste que simula um navegador acessando o seu código
client = TestClient(app)


# TESTE 1: Verifica se a página inicial está acessível (Status 200)
def test_root_status():
    response = client.get("/")
    assert response.status_code == 200


# TESTE 2: Verifica se a mensagem da página inicial está correta
def test_root_content():
    response = client.get("/")
    assert response.json() == {"message": "Sistema de Estudantes Online"}


# TESTE 3: Verifica se a rota de 'saude' retorna o status operacional
def test_health_check():
    response = client.get("/saude")
    assert response.json() == {"status": "operacional"}


# TESTE 4: Simula o cadastro de um estudante e verifica se os dados batem
def test_create_estudante():
    # Dados que vamos enviar para o teste
    payload = {"nome": "Léa Lima", "curso": "DevOps"}
    response = client.post("/estudantes/cadastro", json=payload)

    # Verifica se o servidor aceitou (200) e se o nome retornado é o mesmo
    assert response.status_code == 200
    assert response.json()["nome"] == "Léa Lima"


# TESTE 5: Um teste de lógica simples para validar a integridade do Pytest
def test_logic_simples():
    valor_esperado = 10
    resultado = 5 + 5
    assert resultado == valor_esperado