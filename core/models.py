from django.db import models


class Subscribers(models.Model):
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add= True)
    last_edited= models.DateTimeField(auto_now= True)
