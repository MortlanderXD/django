# django

Web server

## Step 1 : install python

go web

```shell
$python --version

```

## Step 2 : install pipenv # OPTIONNEL

```shell
$pip install pipenv

```

## Step 3 : create Django project

```shell
$mkdir nameProject
$cd nameProject
$pipenv install django
$pipenv shell
$django-admin startproject nameProject .
```

## Step 4 : runsrver port 8000

```shell
$python manage.py runserver 8000
```

## Migrate all new structure to database ( need to do if first time )

```shell
$python manage.py migrate
```

## Creating the admin user and follow instruction

```shell
$python manage.py createsuperuser
```

## Creating the blog app

```shell
$python manage.py startapp blog 
```