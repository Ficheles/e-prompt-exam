PERSONA = """Você é um especialista em análise de consumo de cartões de crédito com vasta experiência em classificação e categorização de despesas financeiras.
Sua tarefa é analisar os dados em formato CSV que contem os detalhes das transações da fatura em <fatura_csv>,
identificar e categorizar cada item de acordo com a lista de categorias fornecida em <categorias>. 
Você é meticuloso, eficiente e atento aos detalhes, garantindo precisão ao classificar transações. 
Além disso, você organiza os dados de forma clara e lógica, facilitando a análise financeira e o planejamento do usuário.
"""

list_categorias = [
    'casa',
    'educação',
    'eletrônicos',
    'lazer',
    'restaurante',
    'saúde',
    'serviços',
    'supermercado',
    'transporte',
    'vestuário',
    'viagem',
    'outros',
]

# Remove "outros"
unhappy_categorias = list_categorias[:-1]

TIPAGEM_UNHAPPY = '''
Se você não achar alguma categoria pertinente, coloque ´INDEFINIDO´
Sua resposta deve ser OBRIGATORIAMENTE a lista em formato json sem ´´´json com base em:
<tipagem>
data: [
    category: str
    date: str
    title: str
    amount: float
]
</tipagem>
'''

HAPPY_CATEGORIAS_PROMPT = '<categorias>' + ','.join(list_categorias) + '</categorias>'
UNHAPPY_CATEGORIAS_PROMPT = '<categorias>' + ','.join(unhappy_categorias) + '</categorias>'
UNHAPPY_PROMPT = UNHAPPY_CATEGORIAS_PROMPT + TIPAGEM_UNHAPPY

def create_prompt(categoria, dados_da_fatura):
    dados_da_fatura = '<fatura_csv>' + dados_da_fatura + '</fatura_csv>'
    return "\n".join([categoria, dados_da_fatura])
