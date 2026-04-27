import os
import sys
# Garante que a pasta 'src' seja encontrada pelo Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app, root, funcaoteste, soma

@pytest.mark.asyncio
async def test_1_helloworld_url():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_2_root_function():
    # Testa a função root diretamente
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_3_status_endpoint():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "online"}

def test_4_funcaoteste_logica():
    # Testa uma função normal (sem async)
    assert funcaoteste() == {"resultado": "sucesso"}

def test_5_soma_simples():
    # Teste matemático simples
    assert soma(2, 3) == 5