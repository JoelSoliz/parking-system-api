from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_settings


config = get_settings()
my_engine = create_engine(
    f"mysql://{config.db_user}:{config.db_password}@{config.db_host}/{config.db_name}"
)

Base = declarative_base()
Session = sessionmaker(my_engine)

if __name__ == "__main__":
    Base.metadata.drop_all(my_engine)
    Base.metadata.create_all(my_engine)
