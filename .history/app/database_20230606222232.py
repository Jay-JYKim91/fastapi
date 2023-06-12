from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:

#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi', user='postgres', password='zkfmak91!', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('database connection was successful')
#     except Exception as error:
#         print('connecting to database failed')
#         print('Error: ', error)
#         time.sleep(2)
