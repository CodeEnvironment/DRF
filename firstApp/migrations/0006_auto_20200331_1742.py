# Generated by Django 2.2.5 on 2020-03-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0005_auto_20200331_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carspecs',
            name='car_addons',
        ),
        migrations.AddField(
            model_name='carspecs',
            name='car_addons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstApp.AddOns'),
        ),
    ]
