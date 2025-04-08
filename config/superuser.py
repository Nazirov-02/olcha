# config/superuser.py

import os
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

def create_superuser():
    try:
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print("✅ Superuser created successfully.")
        else:
            print("ℹ️ Superuser already exists.")
    except (OperationalError, ProgrammingError):
        pass
