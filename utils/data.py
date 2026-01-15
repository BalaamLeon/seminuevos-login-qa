"""Test data and configuration.

Security note:
  Do not hardcode credentials in the repository. Provide them via environment
  variables USER_EMAIL and USER_PASSWORD when running the tests.
"""

import os

home_url = "https://www.seminuevos.com/"
login_url = "https://admin.seminuevos.com/login"

# Credentials must be provided at runtime
email = os.getenv("USER_EMAIL", "")
password = os.getenv("USER_PASSWORD", "")

# Negative test data
invalid_email = "invalid@email.com"
invalid_password = "invalid_password"

error_message = "Usuario o contraseña incorrectos."