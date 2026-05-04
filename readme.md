# Django Example


install Django:
```
python -m pip install Django
```


setup a new Django project and app

```
django-admin startproject example_site
cd example_site
python manage.py startapp blog
```

migrations

```
python manage.py makemigrations
python manage.py migrate
```

this will create a new database file called `db.sqlite3` if you are using the default settings. You can change the database settings in `example_site/settings.py` if you want to use a different database.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    }
}
```

create a superuser to access the admin site

```
python manage.py createsuperuser
```

accessing the admin site at `http://127.0.0.1:8000/admin/` after starting the server and log in with the superuser credentials you just created. You should see the `Post` model that you registered in the admin site.


start server

```
python manage.py runserver
```

## Django REST Framework

install Django REST Framework

```
python -m pip install djangorestframework
```
