# Account APP

## Descripción de las pruebas

- **test_register_user**: Verifica que un nuevo usuario puede registrarse correctamente.
- **test_login_user**: Verifica que un usuario registrado puede iniciar sesión y recibir un token.
- **test_login_user_invalid_credentials**: Verifica que iniciar sesión con credenciales incorrectas devuelve un error.
- **test_get_user_details**: Verifica que un usuario autenticado puede obtener sus detalles de usuario.
- **test_unauthorized_user_details**: Verifica que obtener detalles de usuario sin autenticación devuelve un error.
- **test_logout_user**: Verifica que un usuario autenticado puede cerrar sesión (eliminar su token).
- **test_logout_user_unauthenticated**: Verifica que cerrar sesión sin autenticación devuelve un error.

## Ejecución de las pruebas

Asegúrate de que las pruebas están configuradas correctamente y ejecuta las pruebas con el siguiente comando:

```bash
python manage.py test accounts_api
```

Esto ejecutará las pruebas en el archivo tests.py de la aplicación accounts_api y proporcionará un informe de los resultados en la consola.

# Inventory APP

## Descripción de las pruebas

- **test_create_item**: Verifica que se puede crear un nuevo artículo en el inventario.
- **test_get_all_items**: Verifica que se puede obtener una lista de todos los artículos.
- **test_get_single_item**: Verifica que se pueden obtener los detalles de un artículo específico.
- **test_update_item**: Verifica que se pueden actualizar los detalles de un artículo.
- **test_delete_item**: Verifica que se puede eliminar un artículo.
- **test_create_item_invalid_data**: Verifica que intentar crear un artículo con datos inválidos devuelve un error.
- **test_update_item_invalid_data**: Verifica que intentar actualizar un artículo con datos inválidos devuelve un error.

## Ejecución de las pruebas

Asegúrate de que las pruebas están configuradas correctamente y ejecuta las pruebas con el siguiente comando:

```bash
python manage.py test inventory_api
```

Esto ejecutará las pruebas en el archivo tests.py de la aplicación inventory_api y proporcionará un informe de los resultados en la consola.