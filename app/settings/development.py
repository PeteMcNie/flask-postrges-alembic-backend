# Settings for a development environment. Save this file as `development.ini` and customise to your liking.

# The secret key for securely signing the session cookie. You can get a value to put here like this:
# $ python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = "17236097b9d23bbc1d9ea774e451503222cc48b76d8144d45573982baab2ac55"  # nosec

# The server name that the app will be available at. Don't need for now. Talk to Nigel if needed.
# SERVER_NAME = "app.pineapple.dev.localhost"

# SQLAlchemy settings
# You will need to set up a datebase to use to postgres and reference it here and in the alembic.ini file
SQLALCHEMY_DATABASE_URI = (
    "postgresql://postgres:password@localhost:5431/pineapple?application_name=app"
)
SQLALCHEMY_ECHO = True
