# Generated by Django 3.0.7 on 2020-06-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribers',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
