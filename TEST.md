![img](/static/sendos.png)

---

# Account APP

## Descripción de las pruebas

1. **test_register_user**: Verifica que un nuevo usuario puede registrarse correctamente.
2. **test_login_user**: Verifica que un usuario registrado puede iniciar sesión y recibir un token.
3. **test_login_user_invalid_credentials**: Verifica que iniciar sesión con credenciales incorrectas devuelve un error.

## Ejecución de las pruebas

Ejecuta las pruebas con el siguiente comando:

```
docker-compose exec web python manage.py test accounts_api
```

Esto ejecutará las pruebas en el archivo tests.py de la aplicación accounts_api y proporcionará un informe de los resultados en la consola.

# Inventory APP

## Descripción de las pruebas

1. **test_create_item**: Verifica que se puede crear un nuevo artículo en el inventario.
2. **test_get_all_items**: Verifica que se puede obtener una lista de todos los artículos.
3. **test_get_single_item**: Verifica que se pueden obtener los detalles de un artículo específico.
4. **test_update_item**: Verifica que se puede actualizar completamente un artículo del inventario.
5. **test_partial_update_item**: Verifica que se puede actualizar parcialmente un artículo del inventario.
6. **test_delete_item**: Verifica que se puede eliminar (borrado lógico) un artículo del inventario.
7. **test_create_item_invalid_data**: Verifica que intentar crear un artículo con datos inválidos devuelve un error.
8. **test_update_item_invalid_data**: Verifica que intentar actualizar un artículo con datos inválidos devuelve un error.

## Ejecución de las pruebas

Ejecuta las pruebas con el siguiente comando:

```
docker-compose exec web python manage.py test inventory_api
```

Esto ejecutará las pruebas en el archivo tests.py de la aplicación inventory_api y proporcionará un informe de los resultados en la consola.

---

[Volver al home](../)