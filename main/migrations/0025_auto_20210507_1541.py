# Generated by Django 3.2 on 2021-05-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210507_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestactortorole',
            name='color',
            field=models.CharField(default='yellow', max_length=64),
        ),
        migrations.AddField(
            model_name='requestroletoactor',
            name='color',
            field=models.CharField(default='yellow', max_length=64),
        ),
    ]