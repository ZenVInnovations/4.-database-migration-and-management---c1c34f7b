from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import yaml

Base = declarative_base()

with open("config/db_config.yaml") as f:
    config = yaml.safe_load(f)

db_url = config["database"]["url"]
engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    from core import models
    Base.metadata.create_all(bind=engine)
