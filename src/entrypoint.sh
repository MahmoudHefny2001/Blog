#!/bin/sh

# Wait for the database to be ready
while ! nc -z db 5432; do
  echo "Waiting for the PostgreSQL server to be ready..."
  sleep 1
done

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create a superuser if it doesn't exist
if [ ! -z "$DJANGO_SUPERUSER_USERNAME" ]; then
  python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
fi

# Run the Django server
exec "$@"
