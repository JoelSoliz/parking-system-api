# Stage 1: build dependencies
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as base

WORKDIR /workspace

COPY . .

RUN pip3 install -r requirements.txt

RUN pip3 install -r test-requirements.txt

ENTRYPOINT ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
