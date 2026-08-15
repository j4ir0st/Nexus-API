#!/bin/bash

# Exit on any error
set -o errexit

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
