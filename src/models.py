from sqlalchemy import Integer, String
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.sql.schema import Column
from .database import Base, engine


class Obj(Base):
    __tablename__ = 'retriever_table'

    id = Column(Integer, primary_key=True)
    obj = Column(JSON, nullable=False)


Base.metadata.create_all(engine)
