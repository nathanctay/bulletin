# Generated by Django 4.2.5 on 2024-03-02 09:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletinApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='members',
            field=models.ManyToManyField(related_name='bulletin_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
