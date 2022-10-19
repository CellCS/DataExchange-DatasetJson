from typing import List, Text
from sqlalchemy.sql.expression import text

from sqlalchemy.sql.sqltypes import BOOLEAN, DATE, Date, DateTime, Float, Integer, TEXT
from .database import Base
from sqlalchemy import Column, Integer, String, BLOB, Float

class ExampleFilesTable(Base):
    __tablename__ = 'examples_table'
    FileIndex = Column(Integer, index=True, autoincrement=True)
    FileFullName = Column(String(120),primary_key=True)
    FileName = Column(String(100))
    FileFormat = Column(String(20))
    FileData = Column(BLOB)
    FileExportData = Column(BLOB)
    FileCategory = Column(String(50))
    CreatedTime = Column(Date)
    Note = Column(String(255))