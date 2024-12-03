FROM python:3.12-alpine

ARG token
ENV TOKEN=${token}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

RUN apk add git bash

WORKDIR /home

RUN git clone https://github.com/Ficheles/e-prompt-exam.git .

RUN pip install uv && \
   uv venv && \
   source .venv/bin/activate && \
   uv add guardrails-api-client==0.4.0a1 && \
   uv add guardrails-ai==0.6.0 && \
   guardrails configure --disable-metrics --disable-remote-inferencing --token ${TOKEN} && \
   guardrails hub install hub://guardrails/contains_string

CMD [ "python", "main.py" ]
