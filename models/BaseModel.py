from sqlalchemy.ext.declarative import declarative_base

from engines.Database import Engine

# Base Entity Model Schema
Base = declarative_base()

def init():
  Base.metadata.create_all(bind=Engine)