```sh
docker build --build-arg token=<YOUR-GUARDRAILS_KEY> -t e-prompt .
```


```sh
docker run -it -e OPENAI_API_KEY=<YOUR-OPENAI_API_KEY> e-prompt
```