from typing import List, Text
from sqlalchemy.sql.expression import text

from sqlalchemy.sql.sqltypes import BOOLEAN, DATE, Date, DateTime, Float, Integer, TEXT
from .database import Base
from sqlalchemy import Column, Integer, String, BLOB, Float

class ExampleFilesTable(Base):
    __tablename__ = 'examples_table'
    file_index = Column(Integer, index=True, autoincrement=True)
    file_full_name = Column(String(120),primary_key=True)
    file_name = Column(String(100))
    file_format = Column(String(20))
    file_data = Column(BLOB)
    file_export_data = Column(BLOB)
    file_category = Column(String(50))
    create_time = Column(Date)
    file_note = Column(String(255))