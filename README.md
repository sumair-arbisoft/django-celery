# django-celery
Django using Celery and Celery Beat

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

celery -A celery_poc worker -B --loglevel=info

celery -A celery_poc beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

http://localhost:8000/admin/

Create periodic tasks and enable
