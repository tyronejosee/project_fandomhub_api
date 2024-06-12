<div align="center">
  <a href="https://github.com/tyronejosee/project_new_store#gh-light-mode-only" target="_blank">
    <img src=".github/logo_light.svg" alt="logo-light" width="80">
  </a>
  <a href="https://github.com/tyronejosee/project_new_store#gh-dark-mode-only" target="_blank">
    <img src=".github/logo_dark.svg" alt="logo-dark" width="80">
  </a>
</div>
<div align="center">
  <h1><strong>FandomHub - API</strong></h1>
  <a href="https://project-fandomhub-docs.pages.dev/"><strong>📚 Documentation</strong></a>
</div>
<br>
<p align="center">
An API inspired by MyAnimeList, designed for retrieving detailed information about anime and manga. It provides access to titles, genres, ratings, and user reviews, allowing users to query and explore a wide range of anime and manga content.
<p>
<p align="center">
  <a href="https://www.python.org/">
  <img src="https://img.shields.io/badge/python-3.11.8-blue" alt="python-version">
  </a>
  <a href="https://www.djangoproject.com/">
  <img src="https://img.shields.io/badge/django-5.0.1-green" alt="django-version">
  </a>
  <a href="https://www.django-rest-framework.org/">
  <img src="https://img.shields.io/badge/drf-3.14.0-red" alt="django-version">
  </a>
</p>

## ⚙️ Installation

Clone the repository.

```bash
git clone git@github.com:tyronejosee/project_fandomhub_api.git
```

Create a virtual environment (Optional).

```bash
python -m venv env
```

Activate the virtual environment (Optional).

```bash
env\Scripts\activate
```

Install all dependencies.

```bash
pip install -r requirements/local.txt
```

Create an environment variable file .env.

```bash
SECRET_KEY=""
EMAIL_BACKEND=""
EMAIL_HOST=""
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_PORT=""
EMAIL_USE_TLS=""
```

Docker run.

```bash
(env) docker compose -f docker-compose.dev.yml up
(env) docker compose -f docker-compose.dev.yml up --build
(env) docker compose -f docker-compose.dev.yml stop
(env) docker compose -f docker-compose.dev.yml logs -f
(env) docker compose -f docker-compose.dev.yml start
(env) docker compose -f docker-compose.dev.yml restart <service>
```

Perform database migrations.

```bash
(env) docker compose -f docker-compose.dev.yml exec web bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations*
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate <app_label> <migration_name>
(env) docker compose -f docker-compose.dev.yml exec web python manage.py showmigrations
```

> Note: Create the migrations in case Django skips any.

## 🚀 Usage

Create a superuser to access the entire site without restrictions.

```bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py createsuperuser
```

Log in to `admin`:

```bash
http://127.0.0.1:8000/admin/
```

Access to Swagger o Redoc.

```bash
http://127.0.0.1:8000/api/schema/swagger/
http://127.0.0.1:8000/api/schema/redoc/
```

## 🌍 Internationalization

Generate translation files for the languages.

```bash
(env) django-admin makemessages -l ja --ignore=env/*
(env) django-admin makemessages -l es --ignore=env/*
```

> Use --ignore to exclude specific directories from translation.

Compile translation files after making changes to translations.

```bash
(env) django-admin compilemessages
```

## 🚨 Important Notes

Check the creation of migrations before creating them.

```bash
(env) docker compose -f docker-compose.dev.yml exec web bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations users
(env) docker compose -f docker-compose.dev.yml exec web python manage.py makemigrations
(env) docker compose -f docker-compose.dev.yml exec web python manage.py migrate
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.

## 💾 PostgreSQL

```bash
(env) docker compose -f docker-compose.dev.yml exec web python manage.py dumpdata > backup.json
(env) docker compose -f docker-compose.dev.yml exec web python manage.py loaddata
(env) docker compose -f docker-compose.dev.yml exec db psql -U postgres -d fandomhub_db
(fandomhub_db=#) \dt
(fandomhub_db=#) \d <table>
```

## 💾 Redis

```bash
(env) docker compose exec redis redis-cli
(127.0.0.1:6379) keys *
```

## ⚖️ License

This project is under the [Apache-2.0 license](https://github.com/tyronejosee/project_fandomhub_api/blob/main/LICENSE).
