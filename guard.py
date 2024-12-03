# from typing import Dict, List
# from pydantic import BaseModel
# from guardrails.hub import CsvMatch
# from guardrails import Guard

# # # Create Pydantic BaseModel for Credit Card Expenses

# "name,email\njohn,john@example.com\njane,jane@example.com"

# class LineInput(BaseModel):
#     date: str
#     title: str
#     amount: float

# class CsvInput(BaseModel):
#     data: List[LineInput]

# class CreditCardExpenseOutput(BaseModel):
#     date: str
#     title: str
#     amount: float
#     category: str


# # Initialize Validators
# input_val = CsvMatch()
# output_val = CsvMatch()

# # Create Guards for input and output
# input_guard = Guard.for_pydantic(output_class=CreditCardExpenseInput)
# output_guard = Guard.for_pydantic(output_class=CreditCardExpenseOutput)

# # Run LLM output generating JSON through guards
# input_guard.parse("""
# {
#     "date": "2023-10-01",
#     "title": "Grocery",
#     "amount": 150.00
# }
# """)

# output_guard.parse("""
# {
#     "date": "2023-10-01",
#     "title": "Grocery",
#     "amount": 150.00,
#     "category": "Food"
# }
# """)


# def print_test():
#     # Test input guard
#     input_data = {
#         "date": "2023-10-01",
#         "title": "Grocery",
#         "amount": 150.00
#     }

#     print("Testing input guard with data:", input_data)
#     try:
#         validated_input = input_guard.parse(input_data)
#         print("Input validation successful:", validated_input)
#     except Exception as e:
#         print("Input validation failed:", e)

#     print()  # Line break for readability

#     # Positive test for input guard
#     positive_input_data = {
#         "date": "2023-11-01",
#         "title": "Utilities",
#         "amount": 200.00
#     }

#     print("Testing positive input guard with data:", positive_input_data)
#     try:
#         validated_positive_input = input_guard.parse(positive_input_data)
#         print("Positive input validation successful:", validated_positive_input)
#     except Exception as e:
#         print("Positive input validation failed:", e)

#     print()  # Line break for readability

#     # Test output guard
#     output_data = {
#         "date": "2023-10-01",
#         "title": "Grocery",
#         "amount": 150.00,
#         "category": "Food"
#     }

#     print("Testing output guard with data:", output_data)
#     try:
#         validated_output = output_guard.parse(output_data)
#         print("Output validation successful:", validated_output)
#     except Exception as e:
#         print("Output validation failed:", e)

#     print()  # Line break for readability

#     # Positive test for output guard
#     positive_output_data = {
#         "date": "2023-11-01",
#         "title": "Rent",
#         "amount": 1200.00,
#         "category": "Housing"
#     }

#     print("Testing positive output guard with data:", positive_output_data)
#     try:
#         validated_positive_output = output_guard.parse(positive_output_data)
#         print("Positive output validation successful:", validated_positive_output)
#     except Exception as e:
#         print("Positive output validation failed:", e)

# # Call the print test function
# print_test()

# Import Guard and Validator
# from guardrails.hub import CsvMatch
# from guardrails import Guard
# from guardrails.hub import ContainsString
# from typing import Dict
# from guardrails.validators import (
#     FailResult,
#     PassResult,
#     register_validator,
#     ValidationResult,
# )
# from openai import Stream


# @register_validator(name="categorias_de_gasto", data_type="string")
# def catedorias_de_gasto(texto_a_validar, categorias: list, metadata: Dict) -> ValidationResult:
#     mentioned_words = []
#     for word in categorias:
#         if word not in texto_a_validar:
#             mentioned_words.append(word)

#     if len(mentioned_words) > 0:
#         return FailResult(
#             error_message=f"Categorias não cadastrada: {', '.join(mentioned_words)}",
#         )
#     else:
#         return PassResult()


# categorias = ['transporte', 'mercado', 'farmacia']

# # Setup Guard
# guard = Guard().use_many(
#     catedorias_de_gasto(texto)
# )

# # Validator passes
# guard.validate("name,email\njohn,john@example.com\njane,jane@example.com")
# guard.validate("name,email\njohn\njane,jane@example.com")  # Validator fails



