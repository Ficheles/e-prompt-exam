import os
import csv
import json
from openai import OpenAI
from dotenv import load_dotenv
from guardrails import Guard
from guardrails.errors import ValidationError
from guard import CSVOutput, ValidadorCategorias
from prompt import create_prompt, PERSONA, UNHAPPY_PROMPT, HAPPY_CATEGORIAS_PROMPT


def read_csv_to_string(file_path):
    """Abre um arquivo CSV e retorna seu conteúdo como uma string."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        content = '\n'.join([','.join(row) for row in reader])
    return content


def happy_test(prompt):
    print('\nIniciando HappyTest :)\n')
    guard = Guard.for_pydantic(output_class=CSVOutput)
    try:
        guard(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": PERSONA,
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print('Tudo Passou!!!')
    except ValidationError as e:
        print(e)


def unhappy_test(client: OpenAI, prompt: str):
    print('\nIniciando UnhappyTest :(\n')
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": PERSONA},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = json.loads(completion.choices[0].message.content)
    gua = Guard().use(ValidadorCategorias)
    for i in content:
        try:
            gua.validate(i['category'])
        except ValidationError as e:
            print(e)
            print('Title: ', i['title'], '\n')


if __name__ == '__main__':
    load_dotenv()

    FATURA = read_csv_to_string('gastos_cartao_credito.csv')
    unhappy_prompt = create_prompt(UNHAPPY_PROMPT, FATURA)
    happy_prompt = create_prompt(HAPPY_CATEGORIAS_PROMPT, FATURA)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API não foi encontrada")

    openai_client = OpenAI(api_key=api_key)

    # HAPPY TESTS ##########################################################
    happy_test(happy_prompt)

    input('\nAperte enter para continuar')

    # UNHAPPY TESTS ##########################################################
    unhappy_test(openai_client, unhappy_prompt)
