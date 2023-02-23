#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Create database tables
echo "Apply database migrations"
python manage.py migrate --noinput
# Check if superuser exists
echo "Check if superuser exists"
if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='myadmin').exists())"; then
    echo "Error checking for existing superuser"
    exit 1
fi

# Create superuser
if [ "$(python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='myadmin').exists())")" = "False" ]; then
    echo "Create superuser"
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('myadmin', 'myadmin@example.com', '$(echo $SUPERUSER_PASSWORD)')" | python manage.py shell
else
    echo "Superuser already exists"
fi
