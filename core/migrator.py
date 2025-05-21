from alembic.config import Config
from alembic import command

def get_alembic_config():
    return Config("alembic.ini")

def create_migration(name):
    command.revision(get_alembic_config(), message=name, autogenerate=True)

def apply_migrations():
    command.upgrade(get_alembic_config(), "head")

def rollback(revision="base"):
    command.downgrade(get_alembic_config(), revision)
