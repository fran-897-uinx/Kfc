#!/bin/bash

export $(grep -v '^#' .env | xargs)

python manage.py createsuperuser \
    --username "$DJANGO_SUPERUSER_USERNAME" \
    --email "$DJANGO_SUPERUSER_EMAIL" \
    --noinput

python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); u.set_password('$DJANGO_SUPERUSER_PASSWORD'); u.save()"

echo "Superuser $DJANGO_SUPERUSER_USERNAME created or updated successfully!"
