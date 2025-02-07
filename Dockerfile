# Use uma imagem base do Python
FROM python:3.11-slim-buster

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos de dependência
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação
COPY . .

# Defina a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=portaljm.settings

# Expõe a porta que o Gunicorn vai usar
EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "portaljm.wsgi"]