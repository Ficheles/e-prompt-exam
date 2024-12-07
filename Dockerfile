FROM python:3.12-alpine

ARG token

RUN apk add git bash gcc python3-dev musl-dev linux-headers

WORKDIR /app

RUN git clone https://github.com/Ficheles/e-prompt-exam.git .

RUN pip install uv && \
    uv venv && \
    . .venv/bin/activate && \
    uv add openai && \
    uv add guardrails-ai==0.6.0 && \
    guardrails configure --disable-metrics --disable-remote-inferencing --token ${token}
    
ENTRYPOINT [ "sh", "-c", ". .venv/bin/activate && exec python main.py" ]
