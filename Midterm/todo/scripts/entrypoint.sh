#!/bin/bash

export PYTHONPATH=/app/todo

echo "Waiting for the database to be ready..."
while ! nc -z db 5432; do
  sleep 1
done
echo "Database is ready."

echo "Applying database migrations..."
python todo/manage.py migrate --noinput

echo "Starting Gunicorn server..."
exec gunicorn --workers 4 --bind 0.0.0.0:8000 todo.wsgi:application --certfile=/app/certs/fullchain.pem --keyfile=/app/certs/privkey.pem
