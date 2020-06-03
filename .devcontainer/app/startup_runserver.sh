#!/bin/bash

manage.py migrate
manage.py collectstatic --ignore=*.scss --noinput
manage.py runserver 0.0.0.0:8000