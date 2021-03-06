# Generated by Django 3.2 on 2021-05-06 08:02

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0013_alter_actor_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name', models.CharField(default='', max_length=64, verbose_name='Full name')),
                ('organization', models.CharField(default='', max_length=64, verbose_name='Organization')),
                ('position', models.CharField(default='', max_length=64, verbose_name='Organization')),
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
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=64, verbose_name='Location')),
                ('weight', models.IntegerField(default=0, verbose_name='Weight')),
                ('height', models.IntegerField(default=0, verbose_name='Height')),
                ('sex', models.CharField(choices=[('', 'Not selected'), ('male', 'Male'), ('female', 'Female')], default='', max_length=64, verbose_name='Sex')),
                ('eye_color', models.CharField(choices=[('', 'Not selected'), ('blue', 'Blue'), ('brown', 'Brown'), ('cyan', 'Cyan')], default='', max_length=64, verbose_name='Eye color')),
                ('hair_color', models.CharField(choices=[('', 'Not selected'), ('brunette', 'Brunette'), ('red', 'Red'), ('blond', 'Blond'), ('brown', 'Brown'), ('gray', 'Gray')], default='', max_length=64, verbose_name='Hair color')),
                ('race', models.CharField(choices=[('', 'Not selected'), ('mongoloid', 'Mongoloid'), ('caucasian', 'Caucasian'), ('negroid', 'Negroid')], default='mongoloid', max_length=64, verbose_name='Race')),
                ('nation', models.CharField(default='', max_length=64, verbose_name='Nation')),
                ('body_type', models.CharField(choices=[('', 'Not selected'), ('normal', 'Normal'), ('thin', 'Thin'), ('athletic', 'Athletic'), ('fat', 'Fat')], default='', max_length=64, verbose_name='Body type')),
            ],
        ),
        migrations.AlterField(
            model_name='actor',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 6, 17, 2, 38, 290369), verbose_name='Birthday'),
        ),
    ]
