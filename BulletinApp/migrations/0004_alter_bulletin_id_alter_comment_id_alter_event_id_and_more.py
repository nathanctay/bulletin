# Generated by Django 4.2.5 on 2024-03-02 04:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BulletinApp', '0003_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='BulletinApp.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
