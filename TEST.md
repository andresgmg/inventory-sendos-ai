# Account APP

## Descripción de las pruebas
- test_register_user: Verifica que un nuevo usuario puede registrarse correctamente.
- test_login_user: Verifica que un usuario registrado puede iniciar sesión y recibir un token.
- test_login_user_invalid_credentials: Verifica que iniciar sesión con credenciales incorrectas devuelve un error.
- test_get_user_details: Verifica que un usuario autenticado puede obtener sus detalles de usuario.
- test_get_user_details_unauthenticated: Verifica que obtener detalles de usuario sin autenticación devuelve un error.
- test_logout_user: Verifica que un usuario autenticado puede cerrar sesión (eliminar su token).
- test_logout_user_unauthenticated: Verifica que cerrar sesión sin autenticación devuelve un error.

## Ejecución de las pruebas:
Asegúrate de que tus pruebas están configuradas correctamente y ejecuta las pruebas con el siguiente comando:

```python
python manage.py test accounts_api
```

Esto ejecutará las pruebas en el archivo tests.py de tu aplicación accounts_api y te proporcionará un informe de los resultados.

# Inventory APP