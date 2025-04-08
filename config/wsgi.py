# config/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
application = get_wsgi_application()

# To‘g‘ri import bu yerda:
from config.superuser import create_superuser
create_superuser()
