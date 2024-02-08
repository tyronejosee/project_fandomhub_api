# Project Beehive

## Internationalization

**Generate translation files for the languages:**

```bash
django-admin makemessages -l ja --ignore=env/*
django-admin makemessages -l es --ignore=env/*
```

> Use --ignore to exclude specific directories from translation.

**Compile translation files after making changes to translations:**

```bash
django-admin compilemessages
```

## Important Notes

**Check the creation of migrations before creating them:**

```bash
python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate
```

> Note: Checking migrations before their creation is necessary to avoid inconsistencies in user models.
