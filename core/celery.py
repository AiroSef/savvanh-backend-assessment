import os
from celery import Celery

# set default Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

# Load settings from Django settings.py, using the CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Discover tasks from all installed apps
app.autodiscover_tasks()
