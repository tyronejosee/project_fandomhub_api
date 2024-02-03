# Folder Structure

```txt
project_beehive/
│
├── config/
│   │
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   │
│   ├── .env
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
│
├── apps/
│   │
│   ├── utils/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│   │
│   ├── contents/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── routers.py
│   │   ├── serializers.py
│   │   └── viewsets.py
│   │
│   ├── users/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── rounters.py
│   │   ├── serializers.py
│   │   └── viewsets.py
│   │
│   └── ...
│
├── media/
│
├── docs/
│
├── tests/
│
└── manage.py
```
