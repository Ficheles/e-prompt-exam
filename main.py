from prompt import PROMPT, categorias
from guardrails import Guard
from guardrails.hub import ContainsString
from guard import CSVOutput
from dotenv import load_dotenv

load_dotenv()

guard = Guard.for_pydantic(output_class=CSVOutput)

res = guard(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": PROMPT
    }]
)

print(f"{res.validated_output}")

res.validated_output['data'].append({
    'date': '2024-11-15',
    'title': 'Supermercado Central',
    'amount': 250.75,
    'category': 'teste_fail'})

for line in res.validated_output['data']:
    guard = Guard().use(ContainsString, substring=line['category'], on_fail="exception")
    try:
        guard.validate(','.join(categorias))
    except Exception as e:
        print(e)
