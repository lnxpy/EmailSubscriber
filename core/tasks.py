import string

from core.models import Subscribers
from celery import shared_task
from time import sleep as slp
from django.core.mail import send_mail
from mysite.settings import EMAIL_HOST_USER

@shared_task
def add_email_to_subscribers(email):
    query = Subscribers.objects.create(email=email)
    return ['%s added to Subscribers model!' % (email), 'Ok']

@shared_task
def send_email_to_all(latency=0):
    slp(latency)
    subscribers = Subscribers.objects.all()
    send_mail(
        'This is Title',
        'This is Body',
        EMAIL_HOST_USER, # This is the sender email => Gets from settings.py
        [mail.email for mail in subscribers],
        fail_silently = False,
    )
    return 'I sent emails to all %s Subscribers.' % (subscribers.count())
