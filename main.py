from guardrails import Guard
from prompt import HAPPY_CATEGORIAS_PROMPT, UNHAPPY_CATEGORIAS_PROMPT, PERSONA, create_prompt
from guard import CSVOutput
from dotenv import load_dotenv
import csv

load_dotenv()

def read_csv_to_string(file_path):
    """Abre um arquivo CSV e retorna seu conteúdo como uma string."""
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        content = '\n'.join([','.join(row) for row in reader])
    return content

def run(categorias, dados_fatura):
    prompt = create_prompt(categorias,dados_fatura)
    guard = Guard.for_pydantic(output_class=CSVOutput)
    try:
        result = guard(
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
        print('Tudo Passou!!!\n')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    fatura = read_csv_to_string('gastos_cartao_credito.csv')

    print('\nIniciando Happy Test :)')
    run(HAPPY_CATEGORIAS_PROMPT, fatura)

    input('\n\nAperte enter para continuar')
    
    print('\nIniciando Unhappy Test :)')
    run(UNHAPPY_CATEGORIAS_PROMPT, fatura)

