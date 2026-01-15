# Caso Técnico QA - Login seminuevos.com (Selenium + Python)

Este proyecto automatiza escenarios del formulario de login en:
https://admin.seminuevos.com/login

## Requisitos
- Python 3.10+
- Google Chrome instalado

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```
## Variables de entorno (credenciales)
Por seguridad, **no** se incluyen credenciales en el repositorio. Para ejecutar
las pruebas, define:

- `USER_EMAIL`
- `USER_PASSWORD`

Linux/Mac:
```bash
export USER_EMAIL="tu_correo@dominio.com"
export USER_PASSWORD="tu_password"
```

Windows PowerShell:
```powershell
$env:USER_EMAIL="tu_correo@dominio.com"
$env:USER_PASSWORD="tu_password"
```

## Ejecutar tests
```bash
pytest
```

## Casos cubiertos
- Login exitoso con credenciales válidas
- Login con correo incorrecto (mensaje de error)
- Login con contraseña incorrecta (mensaje de error)
- Submit con campos vacíos (mensaje de error)

## .gitignore recomendado

```gitignore
.venv/
__pycache__/
.pytest_cache/
*.pyc
.DS_Store
```