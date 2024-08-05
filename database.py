from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

URL_DATABASE=os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/QuizApp')


engine=create_engine(URL_DATABASE)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
