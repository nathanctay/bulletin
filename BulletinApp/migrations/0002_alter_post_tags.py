# Generated by Django 4.2.6 on 2024-03-02 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BulletinApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='BulletinApp.tag'),
        ),
    ]
