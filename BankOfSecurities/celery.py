from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab  # Додайте імпорт для розкладу

# Встановлення поточного Django-проекту
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BankOfSecurities.settings')

# Створення екземпляру Celery
app = Celery('BankOfSecurities')

# Завантаження конфігурації Celery з файла налаштувань Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Реєстрація завдань з файлів tasks.py в додатках Django
app.autodiscover_tasks()

# Додайте розклад для функції process_deposits_task
app.conf.beat_schedule = {
    'process-deposits': {
        'task': 'Transaction.tasks.process_deposits_task',
        'schedule': crontab(),  # Розклад запуску: кожен день о 00:00
    },
}