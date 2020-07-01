## EmailSubscriber
Simple Email Sender Built in Celery

### What is EmailSubscriber And How it Works
Imagine your are the admin of this page, so you can add emails, manage them and send them any message you want.
Before using this console, become sure you've already configured both `settings.py` and `tasks.py` truly.
Email Subscriber uses Bootstrap4 for its main panel. Once you turned on your network data, all CDNs will be cached up.

<p align="center">
  <img src="https://github.com/lnxpy/EmailSubscriber/blob/master/pics/p1.png" />
  <small>Home Page (When your server is up)</small>
  </p>

You can add new subscribers by writing their emails in the post form. Once you wrote their email, a message appears and the subscribers table will be updated. A really simple footage is right here.

<p align="center">
  <img src="https://github.com/lnxpy/EmailSubscriber/blob/master/pics/p2.png" />
  <small>Table updated and success message appeared</small>
  </p>

### Danger Zone
In this section, you have a bunch of tools to manage your subscribers.

<p align="center">
  <img src="https://github.com/lnxpy/EmailSubscriber/blob/master/pics/p3.png"/>
  <small>Danger Zone</small>
</p>

#### 1. Send 2 All
By clicking this button, you run a celery task which tries to send an email (which you have configured in `task.py`) to every single subscriber. Once you ran this part, emails will be shown in their inbox as below.

<p align="center">
  <img src="https://github.com/lnxpy/EmailSubscriber/blob/master/pics/e1.png" />
  <small>inbox of eali.iken.908w@ordyspost.ga</small>
  </p>

__Other subscribers will get same email in their inbox__.

Finally, when the `send_email_to_all` task operated, you will see such a result in the Celery console. As you see, in last two lines it responsed "I sent emails to all 3 Subscribers".

<p align="center">
  <img src="https://github.com/lnxpy/EmailSubscriber/blob/master/pics/p4.png"/>
</p>

#### 2. Flush Subscribers
If you want to remove all Subscribers model records, it's a best choice to use this part. As usual, anytime you press this button, subscribers table will be flushed up and nothing will be longer appeared there.

### Setting Up
You may want to setup such a service on your local machine or in production environment. There is no limit. You just need to clone this repo, start configuring and then, you will have a EmailSubscriber in your own platform.

__Docs to setup Celery with Django__
- [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)
- [How to Use Celery and RabbitMQ with Django](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html)
- [Tutorial: Asynchronous Tasks with Django and Celery](https://www.youtube.com/watch?v=WevtkoCA-KQ)

__How to send emails with core.mail.send_mail__
- [Sending Emails in Django](https://www.youtube.com/watch?v=X7DWErkNVJs)
- [Sending email](https://docs.djangoproject.com/en/3.0/topics/email/)

### Fork
Fork and feed for free (never miss the license) :)
