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


## Django ORM

Django ORM (Object-Relational Mapping) is a powerful tool that allows you to interact with your database using Python code instead of writing raw SQL queries. It provides an abstraction layer that makes it easier to work with databases and allows you to define your data models as Python classes.

### select_related

The `select_related` method is used to optimize database queries by performing a SQL join and including related objects in the same query. This can significantly reduce the number of database queries and improve performance when you need to access related objects.

for example:
```
# without select_related
posts = Post.objects.all()
for post in posts:
    print(post.author.name)  # This will cause a separate query for each post to fetch the author

# with select_related
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.name)  # This will fetch the author in the same query, improving performance
```


### prefetch_related

The `prefetch_related` method is used to optimize database queries by performing a separate query for related objects and then joining them in Python. This is useful when you have a many-to-many relationship or when you want to fetch related objects that are not directly related to the main model.

for example:
```
# without prefetch_related
posts = Post.objects.all()
for post in posts:
    print(post.comments.all())  # This will cause a separate query for each post to fetch the comments

# with prefetch_related
posts = Post.objects.prefetch_related('comments').all()
for post in posts:
    print(post.comments.all())  # This will fetch the comments in a separate query and join them in Python, improving performance
```

### annotate

The `annotate` method is used to add additional fields to your querysets based on aggregate functions. This allows you to perform calculations and aggregations on your data directly in the database, which can improve performance and reduce the amount of data that needs to be processed in Python.

for example:
```
from django.db.models import Count
# without annotate
posts = Post.objects.all()
for post in posts:
    print(post.comments.count())  # This will cause a separate query for each post to count the comments

# with annotate
posts = Post.objects.annotate(num_comments=Count('comments')).all()
for post in posts:
    print(post.num_comments)  # This will count the comments in the same query, improving performance
``` 

### aggregate

The `aggregate` method is used to perform aggregate calculations on your querysets and return a dictionary of the results. This allows you to perform calculations such as sums, averages, counts, etc. directly in the database, which can improve performance and reduce the amount of data that needs to be processed in Python.

for example:
```
from django.db.models import Avg

# without aggregate
average_rating = 0
posts = Post.objects.all()
for post in posts:
    average_rating += post.rating
average_rating /= posts.count()  # This will cause a separate query for each post to fetch the rating and then calculate the average in Python

# with aggregate
average_rating = Post.objects.aggregate(Avg('rating'))['rating__avg']  # This will calculate the average rating in the same query, improving performance
``` 


### conclusions

`select_related` -> one-to-one or foreign key relationships, performs a SQL join and includes related objects in the same query.
`prefetch_related` -> many-to-many relationships or when you want to fetch related objects that are not directly related to the main model, performs a separate query for related objects and then joins them in Python.
`annotate` -> adds additional fields to your querysets based on aggregate functions, allows you to perform calculations and aggregations on your data directly in the database.
`aggregate` -> performs aggregate calculations on your querysets and returns a dictionary of the results, allows you to perform calculations such as sums, averages, counts, etc. directly in the database.
