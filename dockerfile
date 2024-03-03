# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo actual al contenedor en /app
COPY . /app

# Instala las dependencias del requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Define el comando a ejecutar cuando se inicia el contenedor
CMD ["python", "app.py"]
