# Django Example


install Django:
```
python -m pip install Django
```


setup a new Django project and app

```
django-admin startproject example_site
cd example_site
python manage.py startapp blogs
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