# Generated by Django 3.2 on 2021-05-06 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_actor_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 21, 2, 28, 903139), verbose_name='Birthday'),
        ),
    ]
