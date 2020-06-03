#!/bin/bash

cd /example
manage.py migrate
manage.py collectstatic --ignore=*.scss --noinput

/etc/init.d/celeryd start
/etc/init.d/celerybeat start

gunicorn --bind 0.0.0.0:8000 budgetapp.wsgi:application