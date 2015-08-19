# My notes

This is a simple chemical compound inventory with fields that I have found useful in lab. It takes structure images from ChemSpider via simple URL, though I intend to update it to use the ChemSpiPy package to also allow more interesting searches (related molecules, etc.). It is currently built for easy deployment to Heroku.

Key technologies I'm learning using this project include search via ElasticSearch engine (searchbox addon in Heroku) and batch import/export via an excel file, through code adapted from [this Google Code project](https://code.google.com/p/django-batchimport/). The batchimport functionality is fairly limited for now, in that it has difficulty with blank/null fields, and I'm still working on understanding how it imports and exports relation fields. It is sufficient for a flat table database, however.

CAREFUL WHEN DEPLOYING: DEBUG IS SET TO TRUE!

# Heroku Django Starter Template

An utterly fantastic project starter template for Django 1.8.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise
- Enhancements to Django's database functionality via django-postgrespool and dj-database-url

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

    $ django-admin.py startproject --template=https://github.com/heroku/heroku-django-template/archive/master.zip --name=Procfile helloworld

You can replace ``helloworld`` with your desired project name.

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [django-postgrespool](https://warehouse.python.org/project/django-postgrespool/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)
