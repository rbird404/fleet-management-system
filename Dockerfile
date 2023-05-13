FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.1.8

RUN apt-get update && apt-get install -y vim && apt-get upgrade -y
RUN pip install --upgrade pip poetry

COPY ./pyproject.toml /pyproject.toml
COPY ./poetry.lock /poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

RUN mkdir -p /src/static
RUN chmod 777 -R /src/static
RUN mkdir -p /src/media && chmod 777 -R /src/media

WORKDIR /src
COPY ./src /src

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "configs.wsgi:application", "--bind", "0:8000"]
