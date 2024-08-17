#!/bin/bash

echo "BUILD START"

# Install dependencies in a local directory
python3.9 -m pip install -r requirements.txt --target ./package

# Navigate into the package directory and zip dependencies
cd package
zip -r9 ../function.zip .

# Navigate back to the root project directory
cd ..

# Add your Django project files to the zip
zip -r9 function.zip .

# Run Django collectstatic command (optional: include this if needed)
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
