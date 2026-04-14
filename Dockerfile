# imagem base
FROM python:3.10

# pasta dentro do container
WORKDIR /app

# copia os arquivos
COPY . .

# comando para rodar o projeto
CMD ["python", "main.py"]