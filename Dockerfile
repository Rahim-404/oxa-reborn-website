# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install build deps then remove cache for smaller image
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 2000

CMD ["gunicorn","app:create_app()" ,"--bind", "0.0.0.0:2000"]