# Generated by Django 3.2 on 2021-05-06 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_actor_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.employer'),
        ),
    ]