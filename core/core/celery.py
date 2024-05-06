import os


from celery import Celery
import django



django.setup()
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# importing tasks bellow
from accounts.tasks import delete_abandon_users

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    time_interval = 60 * 60 * 24
    sender.add_periodic_task(time_interval, delete_abandon_users.s(), name='removes users every 24h')

