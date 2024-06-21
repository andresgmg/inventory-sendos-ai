![img](/static/sendos.png)

---

# Prueba Postulación [Sendos.ai](https://sendos.ai/)

## Prueba Técnica: Desarrollo de una API con Django

## Objetivo

Desarrollar una API RESTful utilizando Django que gestione una simple aplicación de inventario. La aplicación debe permitir crear, leer, actualizar y eliminar (CRUD) artículos en el inventario. Adicionalmente, debe implementar autenticación, pruebas unitarias y despliegue básico utilizando Docker.

## Requerimientos

1. **Modelo de Datos de la tabla "inventory_api_item":**

    - `id`: Identificador único del artículo.
    - `name`: Nombre del artículo.
    - `description`: Descripción del artículo.
    - `quantity`: Cantidad disponible en el inventario.
    - `price`: Precio del artículo.
    - *Datos adicionales agregados para un mejor control*:
        - `is_deleted`: Para manejar el borrado lógico de la base de datos.
        - `created_at`: Información de creación de un ítem.
        - `updated_at`: Información de actualización de un ítem.

2. **Endpoints de la API:**

    - `GET api/v1/inventory/items/`: Obtener la lista de todos los artículos.
    - `POST api/v1/inventory/items/`: Crear un nuevo artículo.
    - `GET api/v1/inventory/items/{id}/`: Obtener detalles de un artículo específico.
    - `PUT api/v1/inventory/items/{id}/`: Actualizar un artículo específico.
    - `DELETE api/v1/inventory/items/{id}/`: Eliminar un artículo específico. (Borrado logico)
    - *Endpoints adicionales para el registro e inicio de sesión con los cuales se obtiene el token*:
        - `POST api/v1/auth/register/`: Registrarse como usuario, retorna un token al ser exitoso.
        - `POST api/v1/auth/login/`: hacer login como usuario, retorna un token al ser exitoso.
    - *Endpoint adicional para inventario*:
        - `PATCH api/v1/inventory/items/{id}/`: Actualizar un campo de un artículo específico.

3. **Autenticación:**

    - Implementar autenticación utilizando JWT (JSON Web Tokens) para proteger los endpoints.
    - **Respuesta:** Fue implementado mediante un registro y un inicio de sesión, los cuales al ser exitosos, retornan un token para utilizar en el resto de los endpoints protegidos.

4. **Pruebas Unitarias:**

    - Escribir pruebas unitarias para los modelos y los endpoints de la API.
    - **Respuesta:** Se realizaron 3 pruebas en `accounts_api` y 8 pruebas en `inventory_api`.

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

## Instalación local de la API REST

1. **Requerimientos:**
    - Python
    - GIT
    - Docker
    - Docker Compose

2. **Instalación:**
    - Clonar el repositorio de GitHub con el comando:
      ```
      git clone https://github.com/andresgmg/inventory-sendos-ai.git
      ```
    - Entrar a la carpeta del proyecto:
      ```
      cd inventory-sendos-ai
      ```
    - Crear un archivo `.env` en la raíz del proyecto. (pedir el archivo al administrador)

3. **Configuración y ejecución con Docker:**
    - Construir y levantar los contenedores con Docker Compose:
      ```sh
      docker-compose up --build
      ```
    - En una terminal separada, aplicar las migraciones:
      ```sh
      docker-compose exec web python manage.py migrate
      ```

4. **Acceso a la API:**
    - La API estará disponible en `http://localhost:8000`.

5. **Comandos adicionales:**
    - Para crear un superusuario de Django:
      ```sh
      docker-compose exec web python manage.py createsuperuser
      ```
    - Para detener los contenedores:
      ```sh
      docker-compose down
      ```
    - Para acceder al contenedor de la web:
      ```sh
      docker-compose exec web sh
      ```

## Link del repositorio GitHub

- [Link del repositorio GitHub](https://github.com/andresgmg/inventory-sendos-ai)

## Links solo de uso con la app corriendo:

- ### Documentación de los Tests realizados

    - [Tests realizados en la API](test/)

- ### Links de Uso de la API REST

    - Documentación en [Redoc](api/v1/docs/redoc/)
    - Documentación en [Swagger](api/v1/docs/swagger/)
