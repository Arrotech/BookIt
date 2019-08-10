import os

from app import bookit_app
from flask_jwt_extended import JWTManager
from app.api.v1.models.database import Database

config_name = os.getenv('APP_SETTINGS')
app = bookit_app(config_name)


@app.cli.command()
def create():
    """Create tables."""

    Database().create_table()

@app.cli.command()
def destroy():
    """Destroy tables."""

    Database().destroy_table()

if __name__ == '__main__':
    app.run(debug=True)
