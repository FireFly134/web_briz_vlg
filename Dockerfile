FROM python:3.11-alpine

ENV PYTHONFAULTHANDLER=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1

WORKDIR /usr/local/app

RUN pip install pipenv
RUN echo "--- ls 1 ---"
RUN ls -la
COPY ./ui/web/Pipfile* ./

RUN pipenv install --system --dev --deploy

COPY ./ui/web/ ./
RUN echo "--- ls 2 ---"
RUN ls -la
RUN chmod u+x ./entrypoint.sh
