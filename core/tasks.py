import string

from core.models import Subscribers
from celery import shared_task
from time import sleep as slp
from django.core.mail import send_mail

@shared_task
def add_email_to_subscribers(email):
    query = Subscribers.objects.create(email=email)
    return '%s added to Subscribers model!' % (email)

@shared_task
def send_email_to_all(latency=0):
    slp(latency)
    subscribers = Subscribers.objects.all()
    send_mail(
        'This is Title',
        'This is Body',
        'alirezayahyapour80@gmail.com', # This is the sender email => Gets from settings.py
        [mail.email for mail in subscribers],
        fail_silently = False,
    )
    return 'I sent emails to all %s Subscribers.' % (subscribers.count())

@shared_task
def flush_database():
    Subscribers.objects.all().delete()
    return 'All subscribers records deleted!'
