# Prueba postulacion [Sendos.ai](https://sendos.ai/)

## Prueba Técnica: Desarrollo de una API con Django

## Objetivo

Desarrollar una API RESTful utilizando Django que gestione una simple aplicación de inventario. La aplicación debe permitir crear, leer, actualizar y eliminar (CRUD) artículos en el inventario. Adicionalmente, debe implementar autenticación, pruebas unitarias y despliegue básico utilizando Docker.

## Requerimientos

1. **Modelo de Datos:**

      - `id`: Identificador único del artículo.
      - `name`: Nombre del artículo.
      - `description`: Descripción del artículo.
      - `quantity`: Cantidad disponible en el inventario.
      - `price`: Precio del artículo.
      - Datos adicionales sugeridos:
        - `is_deleted`: Para manejar el borrado lógico de la DB.
        - `created_at`: Información de creación de un Item.
        - `updated_at`: Información de actualización de un Item.

2. **Endpoints de la API:**

      - `GET /items/`: Obtener la lista de todos los artículos.
      - `POST /items/`: Crear un nuevo artículo.
      - `GET /items/<id>/`: Obtener detalles de un artículo específico.
      - `PUT /items/<id>/`: Actualizar un artículo específico.
      - `DELETE /items/<id>/`: Eliminar un artículo específico.

3. **Autenticación:**

      - Implementar autenticación utilizando JWT (JSON Web Tokens) para proteger los endpoints.

4. **Pruebas Unitarias:**

      - Escribir pruebas unitarias para los modelos y los endpoints de la API.

5. **Despliegue con Docker:**

      - Crear un archivo `Dockerfile` y un archivo `docker-compose.yml` para contenerizar la aplicación y su base de datos (por ejemplo, PostgreSQL).

6. **Documentación:**

      - Proveer documentación sobre cómo configurar y ejecutar el proyecto localmente y cómo usar la API (puede ser un archivo README).

## Evaluación

1. **Correctitud Funcional:**

      - Todos los endpoints deben funcionar según lo especificado.
      - La autenticación debe estar correctamente implementada y proteger los endpoints.

2. **Calidad del Código:**

      - El código debe estar bien organizado, limpio y seguir las mejores prácticas de Django.
      - Utilización adecuada de patrones de diseño y arquitectura.

3. **Pruebas:**

      - Presencia y calidad de las pruebas unitarias.
      - Cobertura de pruebas.

4. **Despliegue:**

      - Correcta implementación de Docker y docker-compose para el despliegue de la aplicación.
      - La aplicación debe ser capaz de ejecutarse correctamente en un entorno Docker.

5. **Documentación:**

      - La documentación debe ser clara y comprensible, facilitando la configuración y el uso del proyecto.

## Duración

Entrega límite: 22 de junio.

## Instalacion local de la API REST
1. **Requerimientos:**
      - Python
      - GIT

2. **Instalacion**
      - bajar el repositorio de GIthub con el comando:
      - entrar a la carpeta y crear el entorno virtual con el comando:
      - activar el entorno virtual con el comando:
      - instalar los requerimientos con el comando:
      - hacer las migraciones con el comando:
      - migrar con el comando:
      - iniciar el servidor de forma local con el comando:

*NOTA: Al ser local no se utiliza Docker y la DB por defecto para el entorno local es SQLite3*

## Link del repositorio Github


## Link de Test realizados

- [Tests realizados en la API](test/)

## Links de Uso de la API REST

- Documentación en [Redoc](api/v1/docs/redoc/)
- Documentación en [Swagger](api/v1/docs/swagger/)

---