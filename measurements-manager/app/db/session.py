from sqlmodel import create_engine
import os

server = os.getenv("POSTGRES_SERVER")
db = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{server}/{db}"


# connect_args = {"check_same_thread": False}
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args=connect_args)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)