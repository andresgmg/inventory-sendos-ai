# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia los archivos de requisitos a la imagen
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de tu proyecto a la imagen
COPY . .

# Expone el puerto en el que Django correrá
EXPOSE 8000

# Comando para ejecutar la aplicación cuando el contenedor se inicie
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "inventory_sendosai.wsgi:application"]