from typing import Callable, Dict, Optional, List
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from prompt import list_categorias

from guardrails.validators import (
    FailResult,
    PassResult,
    register_validator,
    ValidationResult,
    Validator,
)

load_dotenv()

class LineInput(BaseModel):
    date: str
    title: str
    amount: float


class CsvInput(BaseModel):
    data: List[LineInput]


@register_validator(name="validador-categorias", data_type="string")
class ValidadorCategorias(Validator):
    def __init__(self,
                 categorias_a_validar: List[str] = None,
                 on_fail: Optional[Callable] = None):
        super().__init__(on_fail=on_fail)
        self.categorias = categorias_a_validar if categorias_a_validar is not None else list_categorias

    def _validate(self, value: str, metadata: Dict) -> ValidationResult:
        if value.lower() not in self.categorias:
            result = FailResult(
                error_message=f"\nCategoria atribuída: {value}",
            )
        else:
            result = PassResult()

        return result
    
class LineOutput(BaseModel):
    category: str = Field(validators=[ValidadorCategorias()])
    date: str
    title: str
    amount: float

    def __str__(self):
        return f'- {self.category}, {self.title}'


class CSVOutput(BaseModel):
    data: List[LineOutput]

    def __str__(self):
        # Para cada item na lista 'data', chama o método __str__() de LineOutput
        return '\n'.join(str(item) for item in self.data)
