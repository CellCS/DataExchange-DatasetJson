from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import apiconfig as apiconf

apisets = apiconf.APIConfigure()

#engine = create_engine(constants.SQLALCHAMY_DATABASE_URL, connect_args ={"check_same_thread":False})
engine = create_engine(apisets.db_url)
#engine.connect()
#print(engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)
Base = declarative_base()


#docker exec -it mysql_server mysql -uroot -p