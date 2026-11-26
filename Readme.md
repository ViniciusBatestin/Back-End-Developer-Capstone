# Little Lemon — Back-End Developer Capstone

My capstone project for Meta's Back-End Developer Professional Certificate (Coursera, 2025).

A Django web app and REST API for a fictional restaurant, Little Lemon: menu items and table bookings, stored in MySQL and served through Django REST Framework, with token authentication and model tests.

## Stack
Python · Django · Django REST Framework · MySQL

## Run it locally
1. Install dependencies: `pipenv install`
2. Create a MySQL database called `LittleLemon` and update the database settings in `littlelemon/settings.py`
3. Apply migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. Run the tests: `python manage.py test`
6. Create an admin user: `python manage.py createsuperuser`
