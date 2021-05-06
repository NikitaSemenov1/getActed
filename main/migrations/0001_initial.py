# Generated by Django 3.2 on 2021-05-04 07:58

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name1', models.CharField(default='UNNAMED', max_length=64)),
                ('name2', models.CharField(default='UNNAMED', max_length=64)),
                ('name3', models.CharField(default='UNNAMED', max_length=64)),
                ('education', models.CharField(default='UNTITLED', max_length=64)),
                ('location', models.CharField(default='UNTITLED', max_length=64)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
