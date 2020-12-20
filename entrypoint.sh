#!/bin/sh

cd example_auth || return

# Create database migrations
echo "Create database migrations"
python example_auth/manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python example_auth/manage.py migrate


# Start server
echo "Starting server"
python example_auth/manage.py runserver 0.0.0.0:8000