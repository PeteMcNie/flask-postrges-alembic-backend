# Settings for a development environment. Save this file as `development.ini` and customise to your liking.

# The secret key for securely signing the session cookie. You can get a value to put here like this:
# $ python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = "17236097b9d23bbc1d9ea774e451503222cc48b76d8144d45573982baab2ac55"  # nosec

# The server name that the app will be available at.
SERVER_NAME = "app.pineapple.dev.localhost"

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = (
    'postgresql://postgres:password@localhost:5431/pineapple?application_name=app'
    #  "postgresql://spacecadet:spacecadet@db_14/spacecadet?application_name=app" Nigels line not sure about the application name part
)
SQLALCHEMY_ECHO = True