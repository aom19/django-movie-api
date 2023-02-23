#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Create database tables
echo "Apply database migrations"
python manage.py migrate --noinput

# Create superuser
echo "Create superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model();
 User.objects.create_superuser('admin', 'admin@example.com', '$(echo $SUPERUSER_PASSWORD)')" |  python manage.py shell