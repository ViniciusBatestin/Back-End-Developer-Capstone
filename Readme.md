# Little Lemon — Back-End Developer Capstone

My capstone project for Meta's Back-End Developer Professional Certificate (Coursera, 2025).

A Django web app and REST API for a fictional restaurant, Little Lemon: a menu and table bookings stored in MySQL and served through Django REST Framework, with token authentication via Djoser and model tests.

## Stack
Python · Django · Django REST Framework · Djoser · MySQL

## Screenshots

### Website
<img width="1600" height="888" alt="capstone-home" src="https://github.com/user-attachments/assets/4e0163af-d957-469f-b23a-74aa31d2fd43" />

### REST API
<img width="1600" height="1313" alt="capstone-api" src="https://github.com/user-attachments/assets/edce9bc3-a633-4b7c-820f-64ea2b306668" />

### Admin panel
<img width="1600" height="734" alt="capstone-admin" src="https://github.com/user-attachments/assets/6eb9f1e9-b279-4980-9427-c2e5b40204d5" />

## API endpoints

| Endpoint | What it does |
| --- | --- |
| `/restaurant/` | Website home page |
| `/restaurant/menu/` | List menu items (GET) or add one (POST) |
| `/restaurant/menu/<id>` | View, update or delete a single menu item |
| `/restaurant/booking/tables/` | Table bookings (requires a token) |
| `/restaurant/api-token-auth/` | Get an auth token with username and password |
| `/auth/users/` | Register a user (Djoser) |
| `/auth/token/login/` | Log in and get a token (Djoser) |
| `/admin/` | Django admin |

## Run it locally
1. Install dependencies: `pipenv install`
2. Create a MySQL database called `LittleLemon` and update the database settings in `littlelemon/settings.py`
3. Apply migrations: `pipenv run python manage.py migrate`
4. Create an admin user: `pipenv run python manage.py createsuperuser`
5. Start the server: `pipenv run python manage.py runserver`
6. Run the tests: `pipenv run python manage.py
