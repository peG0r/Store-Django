#!/usr/bin/env bash


# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
echo "Building the project..."
python3.9 -m pip install -r requirements.txt


echo "Makr Migrations..."
# Apply any outstanding database migrations
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput


# Convert static asset files
echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear
