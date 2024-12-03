from python:3.12-alpine

RUN apk add bash curl nano 

WORKDIR /home/projeto

RUN git clone https://github.com/Ficheles/e-prompt-exam.git
RUN pip install uv && uv venv && source .venv/bin/activate && uv sync

CMD ['python', 'main.py']
