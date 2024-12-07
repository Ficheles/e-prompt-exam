# E-Prompt

## Descrição do Projeto
O E-Prompt é um projeto destinado a analisar dados financeiros de transações de cartões de crédito e classificar essas despesas utilizando os modelos de linguagem da OpenAI. O projeto permite aos usuários compreender melhor seus hábitos de gasto através da categorização automatizada de despesas.

## Funcionalidades Principais
- Leitura de dados de transações de arquivos CSV.
- Geração de prompts para classificação de despesas.
- Validação dos resultados de classificação.

## Estrutura do Projeto
```plaintext
e-prompt/
│
├── main.py
├── prompt.py
├── gastos_cartao_credito.csv
├── README.md
├── Dockerfile
└── testes.ipynb
```

## Como Funciona
1. **Configuração**: O usuário deve seguir as instruções fornecidas no `README.md` para configurar o ambiente usando o Docker, garantindo que todas as dependências sejam instaladas corretamente.
2. **Entrada de Dados**: Os dados de transações são fornecidos no arquivo `gastos_cartao_credito.csv`, que é lido pela aplicação.
3. **Geração de Prompts**: A aplicação gera prompts com base nos dados de transação usando o arquivo `prompt.py`.
4. **Classificação**: Os prompts são enviados à API OpenAI para processamento, categorizando cada transação em categorias definidas.
5. **Validação**: Os resultados são validados para garantir que todas as transações tenham sido categorizadas corretamente.

## Como Configurar o Projeto
Para configurar e executar o E-Prompt, siga os passos abaixo:

### Pré-requisitos
- Docker instalado no seu sistema.

### Construção e Execução
Execute os seguintes comandos no terminal:

```sh
# Salvar sua chave openai no ambiente
export OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>

# Salvar seu token guardrails no ambiente
export GUARDRAILS_TOKEN=<YOUR-GUARDRAILS-TOKEN>

# Fazer o guild da sua imagem docker utilizando GUARDRAILS_TOKEN
docker build --build-arg token=$GUARDRAILS_TOKEN -t e-prompt .

# Criar seu container docker utilizando sua chave openai
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY e-prompt
```

Substitua `<YOUR-GUARDRAILS_KEY>` e `<YOUR-OPENAI_API_KEY>` pelas chaves apropriadas.

## Como Usar
1. **Preparar Dados**: Coloque seus dados de transações no arquivo `gastos_cartao_credito.csv` no formato adequado.
2. **Executar o Projeto**: Após a configuração, o projeto processará automaticamente as transações, classificando-as nas categorias especificadas.
3. **Verificação de Resultados**: Utilize o notebook `testes.ipynb` para testar e validar a funcionalidade da aplicação, além de revisar os resultados da classificação.

## Explicação dos Arquivos
- `main.py`: Ponto de entrada da aplicação que integra os componentes para processar os dados de transações.
- `prompt.py`: Define os prompts usados para classificação e gera entradas estruturadas para a API OpenAI.
- `gastos_cartao_credito.csv`: Contém as transações financeiras que devem ser analisadas.
- `Dockerfile`: Especifica a configuração de ambiente necessária para executar a aplicação.
- `testes.ipynb`: Um notebook Jupyter usado para testar e validar a funcionalidade do aplicativo.

## Conclusão
O E-Prompt é uma ferramenta poderosa que permite aos usuários analisar suas despesas de cartão de crédito de forma eficiente. Seguindo as instruções acima, você poderá configurar e usar o projeto com facilidade, proporcionando uma melhor compreensão de seus hábitos financeiros.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests no repositório.