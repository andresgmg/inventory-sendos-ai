# Usa una imagen base oficial de Python
FROM python:3.12

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo requirements.txt a la imagen
COPY requirements.txt .

# Actualiza pip y luego instala las dependencias
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación a la imagen
COPY . .

# Expone el puerto en el que Django se ejecuta
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "debug", "inventory_sendosai.wsgi:application"]
