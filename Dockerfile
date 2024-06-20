# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de requerimientos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al contenedor
COPY . /app/

# Exponer el puerto que Django usa (por defecto es 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8000", "inventory_sendosai.wsgi:application"]
