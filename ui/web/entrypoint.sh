#!/bin/sh
#python manage.py makemigrations
python manage.py migrate
celery -A web.celery:app worker -B -l info --detach
python manage.py runserver 0.0.0.0:8000