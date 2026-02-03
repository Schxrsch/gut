FROM python:3.11-slim

WORKDIR /app
RUN pip install --no-cache-dir sympy

COPY benchmark.py /app/benchmark.py

CMD ["sleep", "infinity"]
