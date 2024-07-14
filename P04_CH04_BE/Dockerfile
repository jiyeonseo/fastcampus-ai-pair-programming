ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry \
    && poetry install --no-root

COPY . .

EXPOSE 8080

CMD ["./entrypoint.sh"]
