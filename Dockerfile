# Stage 1: build dependencies
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10 as base

WORKDIR /workspace

COPY . .

RUN pip3 install -r requirements.txt

RUN pip3 install -r test-requirements.txt

WORKDIR /workspace/parking_system

ENTRYPOINT ["/bin/bash", "-c", "trap : TERM INT; sleep infinity & wait"]
