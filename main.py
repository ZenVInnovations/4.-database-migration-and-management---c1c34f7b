import typer
from core.db import init_db
from core.migrator import create_migration, apply_migrations, rollback

app = typer.Typer()

@app.command()
def init():
    init_db()
    print("Database initialized.")

@app.command()
def makemigration(name: str):
    create_migration(name)

@app.command()
def migrate():
    apply_migrations()

@app.command()
def downgrade(revision: str = "base"):
    rollback(revision)

if __name__ == "__main__":
    app()
