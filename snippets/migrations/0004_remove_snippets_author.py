# Generated by Django 3.1.2 on 2021-05-15 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20210515_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippets',
            name='author',
        ),
    ]
