#!/bin/bash 

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"prevailfrancis@gmail.com"}

/opt/env/Scripts/python manage.py migrate --noinput 

/opt/env/Scripts/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

