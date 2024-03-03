FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/local/app

RUN pip install pipenv
COPY ./ui/web/Pipfile* ./

RUN pipenv install --system --dev --deploy

COPY ./ui/web/ .

RUN chmod u+x ./ui/web/entrypoint.sh
