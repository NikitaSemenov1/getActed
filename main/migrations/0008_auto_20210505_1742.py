# Generated by Django 3.2 on 2021-05-05 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210505_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='name1',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='actor',
            name='name3',
        ),
        migrations.AddField(
            model_name='actor',
            name='name',
            field=models.CharField(default='NONE', max_length=64, verbose_name='Полное имя'),
        ),
        migrations.AlterField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 17, 42, 28, 898505)),
        ),
    ]