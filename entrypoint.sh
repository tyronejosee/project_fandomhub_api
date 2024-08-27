#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

# Apply database migrations using Django's manage.py script
python manage.py migrate

# Collect static files from each app into a single location (for serving in production), suppressing prompts
python manage.py collectstatic --noinput

# Add the cron jobs defined in Django's crontab configuration
python manage.py crontab add

# Start the Django development server on all network interfaces, listening on port 8000
python manage.py runserver 0.0.0.0:8000

# Start the Gunicorn server, which is a production WSGI HTTP server for Django,
# binding to all network interfaces on port 8000
# exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
