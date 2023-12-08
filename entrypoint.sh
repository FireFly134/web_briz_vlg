#!/bin/sh
celery -A taskmanager.celery:app worker -B -l info --detach
python manage.py runserver 0.0.0.0:8000