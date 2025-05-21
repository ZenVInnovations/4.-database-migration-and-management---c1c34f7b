from core.db import SessionLocal
from core.models import User

def load_sample_data():
    db = SessionLocal()
    users = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com"),
        User(name="Charlie", email="charlie@example.com"),
    ]
    db.add_all(users)
    db.commit()
    db.close()

if __name__ == '__main__':
    load_sample_data()
    print("Sample users added.")
