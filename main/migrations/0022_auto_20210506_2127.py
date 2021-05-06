# Generated by Django 3.2 on 2021-05-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_requestactortorole_requestroletoactor'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestactortorole',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestactortorole',
            name='is_denied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestroletoactor',
            name='is_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestroletoactor',
            name='is_denied',
            field=models.BooleanField(default=False),
        ),
    ]