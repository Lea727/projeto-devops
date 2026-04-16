# imagem base
FROM python:3.10

# pasta dentro do container
WORKDIR /app

# Primeiro tratamos das dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Depois copiamos o código
COPY . .

# comando para rodar o projeto
CMD ["python", "main.py"]