Shop Application built with Django 4 by Example, supporting Celery, RabbitMQ, sessions, and full authentication.
This project follows production-ready patterns and includes modern e-commerce features.

Table of Contents

Features

Installation

Images

Features

Session-based shopping cart

Product catalog with categories

Order creation and checkout workflow

Celery integration to process asynchronous tasks

RabbitMQ as message broker for Celery

Sending order notifications using Celery tasks

Django built-in authentication (login–register–logout)

Profile page for customers

Editing user profile

Full password reset & password change system

Running the Django development server using HTTPS

Secure and scalable project structure based on Django 4 by Example

Installation

Clone the repository:

git clone https://github.com/yahiahamdan/shop-project.git


Navigate to the project directory:

cd shop


Create and activate a virtual environment:

python -m venv env
.\env\Scripts\activate      # On Windows
# OR
source env/bin/activate     # On macOS / Linux


Install the required packages:

pip install -r requirements.txt


Start RabbitMQ server:

rabbitmq-server


Start Celery worker:

celery -A shop worker -l info


Apply migrations:

python manage.py migrate


Create a superuser:

python manage.py createsuperuser


Run the development server (HTTPS optional):

python manage.py runserver_plus --cert-file cert.pem --key-file key.pem


Open your browser and visit:

https://localhost:8000/
