from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class LineInput(BaseModel):
    date: str
    title: str
    amount: float


class CsvInput(BaseModel):
    data: List[LineInput]


class LineOutput(BaseModel):
    date: str
    title: str
    amount: float
    category: str


class CSVOutput(BaseModel):
    data: List[LineOutput]

