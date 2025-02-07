# Usar una imagen base ligera
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto necesario (por defecto, Streamlit usa el puerto 8501)
EXPOSE 8501

# Comando para ejecutar Streamlit
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]