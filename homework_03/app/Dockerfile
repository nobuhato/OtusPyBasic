#docker build . -t book_app

FROM python:3.9.6-buster

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./book_app/pyproject.toml .
COPY ./book_app/poetry.lock .

COPY book_app ./

RUN poetry install

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]