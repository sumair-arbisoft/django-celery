# django-celery
Django using Celery and Celery Beat

Create a virtual environment and install dependencies

```
python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py createsuperuser
```
### Terminal 1:

`python3 manage.py runserver`

### Terminal 2:

`celery -A celery_poc worker -B --loglevel=info`

### Terminal 3:

`celery -A celery_poc beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler`

### Admin Panel:

http://localhost:8000/admin/

Create periodic tasks and enable
