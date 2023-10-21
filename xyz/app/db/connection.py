from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_URL = config('POSTGRES_URL')
engine = create_engine(POSTGRES_URL, pool_pre_ping=True)
Session = sessionmaker()