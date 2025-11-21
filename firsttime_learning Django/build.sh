#!/bin/bash 

echo "collecting static files..............."
python manage.py collectstatic  --noinput 


echo "Building tailwind........"

python manage.py tailwind build 

echo "creating superuser..............."
./createuser.sh


echo "creaiting migrations..............."
python manage.py makemigrations
python manage.py migrate


echo "Build completed successfully!"