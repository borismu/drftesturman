# Project with DRF

## How to prepare for testing a repository
After cloning repository run following commands and follow prompts to setup credentials for admin user

docker-compose up --build

docker-compose run django python manage.py createsuperuser


## How to test api
Go to **localhost:8000/api/applications/** and use admin credentials from previous step to view all applications. 

In order to create application POST to **localhost:8000/api/applications/** with JSON containing name and id.

In order to update/delete application with ID UPDATE/DELETE to **localhost:8000/api/applications/ID/**

## How to GET /api/test/

Visit **localhost:8000/api/test/?api_key=API_KEY_HERE**
