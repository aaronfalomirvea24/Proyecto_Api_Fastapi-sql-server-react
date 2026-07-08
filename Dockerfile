# 1. Usamos Ubuntu de base (Mucho más amigable con los drivers de Microsoft)
FROM ubuntu:22.04

# Evitar que el instalador de paquetes se quede esperando interacción del usuario
ENV DEBIAN_FRONTEND=noninteractive

# 2. Instalar Python y dependencias básicas del sistema
RUN apt-get update && apt-get install -y \
    python3.11 \
    python3-pip \
    python3.11-dev \
    curl \
    gnupg2 \
    unixodbc \
    unixodbc-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3. Agregar repositorio de Microsoft e instalar msodbcsql18
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# 4. Configurar el directorio de trabajo
WORKDIR /app

# 5. Copiar e instalar las dependencias de Python
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt

# 6. Copiar todo el código de tu API
COPY . .

# 7. Comando para arrancar FastAPI apuntando a tu app
CMD python3.11 -m uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
