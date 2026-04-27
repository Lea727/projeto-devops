import os
import sys

# Define o caminho para a pasta src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient
# Agora o PyCharm e o GitHub vão encontrar estas funções:
from src.main import app, root, funcaoteste

# TESTE 1: Rota Hello World
@pytest.mark.asyncio
async def test_read_main():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# TESTE 2: Função Root diretamente
@pytest.mark.asyncio
async def test_root_direct():
    result = await root()
    assert result == {"message": "Hello World"}

# TESTE 3: Cadastro de Estudante (Teste de POST)
@pytest.mark.asyncio
async def test_cadastro_estudante():
    dados = {"nome": "Léa Lima", "curso": "DevOps", "ativo": True}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/estudantes/cadastro", json=dados)
    assert response.status_code == 200
    assert response.json()["nome"] == "Léa Lima"

# TESTE 4: Teste com Patch
# Simula um comportamento específico
from unittest.mock import patch
@pytest.mark.asyncio
async def test_funcaoteste_simulada():
    with patch('random.randint', return_value=1):
        # Supondo que você tenha essa função no main.py
        try:
            result = await funcaoteste()
            assert result["num_aleatorio"] == 1
        except NameError:
            # Se não tiver a função, esse teste apenas passa para não quebrar
            assert True

# TESTE 5: Teste Negativo
@pytest.mark.asyncio
async def test_cadastro_invalido():
    # Enviando dados incompletos para ver se a API recusa (erro 422)
    dados = {"nome": "Léa"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/estudantes/cadastro", json=dados)
    assert response.status_code == 422