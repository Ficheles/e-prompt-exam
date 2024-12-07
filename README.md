
Salvar sua chave openai no ambiente
```sh
export OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>
```

Salvar seu token guardrails no ambiente
```sh
export GUARDRAILS_TOKEN=<YOUR-GUARDRAILS-TOKEN>
```

Fazer o guild da sua imagem docker utilizando GUARDRAILS_TOKEN
```sh
docker build --build-arg token=$GUARDRAILS_TOKEN -t e-prompt .
```

Criar seu container docker utilizando sua chave openai
```sh
docker run -it -e OPENAI_API_KEY=$OPENAI_API_KEY e-prompt
```
