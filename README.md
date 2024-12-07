# E-Prompt ![alt text](./img/Guardrails-ai-logo-for-dark-bg.svg)

![alt text](./img/guardrails.png)

## Descrição do Projeto

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-74aa9c?logo=openai&logoColor=white)](#)
[![Guardrails](https://img.shields.io/badge/Guardrails-888?logoColor=fff&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjQiIGhlaWdodD0iNjQiIHZpZXdCb3g9IjAgMCA2NCA2NCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzFfMzQ1NykiPgo8cGF0aCBkPSJNNjMuMDgxMiAzMS41NDA3QzYzLjA4MTIgNDguOTYwMSA0OC45NiA2My4wODE0IDMxLjU0MDUgNjMuMDgxNEMxNy40MTc3IDYzLjA4MTQgNS40NjI5MSA1My43OTkzIDEuNDQzNzkgNDEuMDAyOUg4LjE0MjEzQzExLjg4NTMgNTAuMjUwMSAyMC45NTExIDU2Ljc3MzIgMzEuNTQwNSA1Ni43NzMyQzQ1LjQ3NjEgNTYuNzczMiA1Ni43NzMxIDQ1LjQ3NjIgNTYuNzczMSAzMS41NDA3QzU2Ljc3MzEgMTcuNjA1MSA0NS40NzYxIDYuMzA4MTQgMzEuNTQwNSA2LjMwODE0QzIwLjk1MTEgNi4zMDgxNCAxMS44ODUzIDEyLjgzMTMgOC4xNDIxMiAyMi4wNzg1SDEuNDQzNzhDNS40NjI4OSA5LjI4MjA5IDE3LjQxNzcgMCAzMS41NDA1IDBDNDguOTYgMCA2My4wODEyIDE0LjEyMTIgNjMuMDgxMiAzMS41NDA3Wk0wLjE1NTczNSAzNC42OTQ3QzAuMDUyNzM3OSAzMy42NTczIDAgMzIuNjA1MSAwIDMxLjU0MDZDMCAzMC40NzYxIDAuMDUyNzM3OSAyOS40MjQgMC4xNTU3MzUgMjguMzg2NkgxMi44Nzc5QzE0LjM3OTUgMTkuNDM2MiAyMi4xNjM3IDEyLjYxNjIgMzEuNTQwNyAxMi42MTYyQzM4LjU0NTQgMTIuNjE2MiA0NC42NjEyIDE2LjQyMTkgNDcuOTMzNCAyMi4wNzg0SDM5Ljg4NThDMzcuNjYxOCAyMC4xMTU1IDM0Ljc0MDMgMTguOTI0NCAzMS41NDA3IDE4LjkyNDRDMjQuNTcyOSAxOC45MjQ0IDE4LjkyNDQgMjQuNTcyOSAxOC45MjQ0IDMxLjU0MDZDMTguOTI0NCAzOC41MDg0IDI0LjU3MjkgNDQuMTU2OSAzMS41NDA3IDQ0LjE1NjlDMzcuNDE5NCA0NC4xNTY5IDQyLjM1OSA0MC4xMzYyIDQzLjc1OTUgMzQuNjk0N0gzMy41OTA4VjI4LjM4NjZINTAuMjAzNEM1MC4zNzU1IDI5LjQxMjMgNTAuNDY1MSAzMC40NjYgNTAuNDY1MSAzMS41NDA2QzUwLjQ2NTEgNDEuOTkyMyA0MS45OTI0IDUwLjQ2NSAzMS41NDA3IDUwLjQ2NUMyMi4xNjM3IDUwLjQ2NSAxNC4zNzk1IDQzLjY0NSAxMi44Nzc5IDM0LjY5NDdIMC4xNTU3MzVaIiBmaWxsPSIjMzlGRkMwIi8+CjxwYXRoIGQ9Ik02My4wODEyIDMxLjU0MDdDNjMuMDgxMiA0OC45NjAxIDQ4Ljk2IDYzLjA4MTQgMzEuNTQwNSA2My4wODE0QzE3LjQxNzcgNjMuMDgxNCA1LjQ2MjkxIDUzLjc5OTMgMS40NDM3OSA0MS4wMDI5SDguMTQyMTNDMTEuODg1MyA1MC4yNTAxIDIwLjk1MTEgNTYuNzczMiAzMS41NDA1IDU2Ljc3MzJDNDUuNDc2MSA1Ni43NzMyIDU2Ljc3MzEgNDUuNDc2MiA1Ni43NzMxIDMxLjU0MDdDNTYuNzczMSAxNy42MDUxIDQ1LjQ3NjEgNi4zMDgxNCAzMS41NDA1IDYuMzA4MTRDMjAuOTUxMSA2LjMwODE0IDExLjg4NTMgMTIuODMxMyA4LjE0MjEyIDIyLjA3ODVIMS40NDM3OEM1LjQ2Mjg5IDkuMjgyMDkgMTcuNDE3NyAwIDMxLjU0MDUgMEM0OC45NiAwIDYzLjA4MTIgMTQuMTIxMiA2My4wODEyIDMxLjU0MDdaTTAuMTU1NzM1IDM0LjY5NDdDMC4wNTI3Mzc5IDMzLjY1NzMgMCAzMi42MDUxIDAgMzEuNTQwNkMwIDMwLjQ3NjEgMC4wNTI3Mzc5IDI5LjQyNCAwLjE1NTczNSAyOC4zODY2SDEyLjg3NzlDMTQuMzc5NSAxOS40MzYyIDIyLjE2MzcgMTIuNjE2MiAzMS41NDA3IDEyLjYxNjJDMzguNTQ1NCAxMi42MTYyIDQ0LjY2MTIgMTYuNDIxOSA0Ny45MzM0IDIyLjA3ODRIMzkuODg1OEMzNy42NjE4IDIwLjExNTUgMzQuNzQwMyAxOC45MjQ0IDMxLjU0MDcgMTguOTI0NEMyNC41NzI5IDE4LjkyNDQgMTguOTI0NCAyNC41NzI5IDE4LjkyNDQgMzEuNTQwNkMxOC45MjQ0IDM4LjUwODQgMjQuNTcyOSA0NC4xNTY5IDMxLjU0MDcgNDQuMTU2OUMzNy40MTk0IDQ0LjE1NjkgNDIuMzU5IDQwLjEzNjIgNDMuNzU5NSAzNC42OTQ3SDMzLjU5MDhWMjguMzg2Nkg1MC4yMDM0QzUwLjM3NTUgMjkuNDEyMyA1MC40NjUxIDMwLjQ2NiA1MC40NjUxIDMxLjU0MDZDNTAuNDY1MSA0MS45OTIzIDQxLjk5MjQgNTAuNDY1IDMxLjU0MDcgNTAuNDY1QzIyLjE2MzcgNTAuNDY1IDE0LjM3OTUgNDMuNjQ1IDEyLjg3NzkgMzQuNjk0N0gwLjE1NTczNVoiIHN0cm9rZT0iIzM5RkZDMCIvPgo8L2c+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzFfMzQ1NyI+CjxyZWN0IHdpZHRoPSI2NCIgaGVpZ2h0PSI2NCIgZmlsbD0id2hpdGUiLz4KPC9jbGlwUGF0aD4KPC9kZWZzPgo8L3N2Zz4K)](#)


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