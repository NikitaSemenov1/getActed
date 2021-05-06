from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

NONE_VALUE = ''


class Actor(User):
    name = models.CharField(max_length=64, default="NONAME", verbose_name="Full name")
    education = models.CharField(max_length=64, default=NONE_VALUE, verbose_name="Education")
    location = models.CharField(max_length=64, default=NONE_VALUE, verbose_name="Location")
    birth_date = models.DateField(default=date(2000, 1, 1), verbose_name="Birthday")
    # Look

    weight = models.IntegerField(default=0, verbose_name="Weight")
    height = models.IntegerField(default=0, verbose_name="Height")

    SEX_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('male', 'Male'),
        ('female', 'Female')
    ]

    sex = models.CharField(max_length=64, choices=SEX_CHOICES, default=NONE_VALUE, verbose_name="Sex")

    EYE_COLOR_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
        ('cyan', 'Cyan'),
    ]

    eye_color = models.CharField(max_length=64, choices=EYE_COLOR_CHOICES, default=NONE_VALUE, verbose_name="Eye color")

    HAIR_COLOR_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('brunette', 'Brunette'),
        ('red', 'Red'),
        ('blond', 'Blond'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
    ]

    hair_color = models.CharField(max_length=64, choices=HAIR_COLOR_CHOICES, default=NONE_VALUE, verbose_name="Hair color")

    RACE_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('mongoloid', 'Mongoloid'),
        ('caucasian', 'Caucasian'),
        ('negroid', 'Negroid'),
    ]

    race = models.CharField(max_length=64, choices=RACE_CHOICES, default='mongoloid', verbose_name="Race")
    nation = models.CharField(max_length=64, default=NONE_VALUE, verbose_name="Nation")

    BODY_TYPE_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('normal', 'Normal'),
        ('thin', 'Thin'),
        ('athletic', 'Athletic'),
        ('fat', 'Fat'),
    ]

    body_type = models.CharField(max_length=64, choices=BODY_TYPE_CHOICES, default=NONE_VALUE, verbose_name="Body type")

    def __str__(self):
        return self.name

    @property
    def get_age(self):
        delta = relativedelta(datetime.today(), self.birth_date)
        return delta.years


class Employer(User):
    name = models.CharField(max_length=64, default="NONAME", verbose_name="Full name")
    organization = models.CharField(max_length=64, default=NONE_VALUE, verbose_name='Organization')
    position = models.CharField(max_length=64, default=NONE_VALUE, verbose_name='Position')

    def __str__(self):
        return self.name


class Role(models.Model):
    title = models.CharField(max_length=64, default=NONE_VALUE, verbose_name='Title')
    description = models.TextField(max_length=256, default=NONE_VALUE, verbose_name='Description')

    location = models.CharField(max_length=64, default=NONE_VALUE, verbose_name='Location')
    creator = models.ForeignKey(Employer, on_delete=models.CASCADE, default=1)
    # Look

    weight = models.IntegerField(default=0, verbose_name="Weight")
    height = models.IntegerField(default=0, verbose_name="Height")

    SEX_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('male', 'Male'),
        ('female', 'Female')
    ]

    sex = models.CharField(max_length=64, choices=SEX_CHOICES, default=NONE_VALUE, verbose_name="Sex")

    EYE_COLOR_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('blue', 'Blue'),
        ('brown', 'Brown'),
        ('cyan', 'Cyan'),
    ]

    eye_color = models.CharField(max_length=64, choices=EYE_COLOR_CHOICES, default=NONE_VALUE, verbose_name="Eye color")

    HAIR_COLOR_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('brunette', 'Brunette'),
        ('red', 'Red'),
        ('blond', 'Blond'),
        ('brown', 'Brown'),
        ('gray', 'Gray'),
    ]

    hair_color = models.CharField(max_length=64, choices=HAIR_COLOR_CHOICES, default=NONE_VALUE,
                                  verbose_name="Hair color")

    RACE_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('mongoloid', 'Mongoloid'),
        ('caucasian', 'Caucasian'),
        ('negroid', 'Negroid'),
    ]

    race = models.CharField(max_length=64, choices=RACE_CHOICES, default='mongoloid', verbose_name="Race")
    nation = models.CharField(max_length=64, default=NONE_VALUE, verbose_name="Nation")

    BODY_TYPE_CHOICES = [
        (NONE_VALUE, 'Not selected'),
        ('normal', 'Normal'),
        ('thin', 'Thin'),
        ('athletic', 'Athletic'),
        ('fat', 'Fat'),
    ]

    body_type = models.CharField(max_length=64, choices=BODY_TYPE_CHOICES, default=NONE_VALUE, verbose_name="Body type")

    def __str__(self):
        return self.title


class RequestActorToRole(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    status = models.CharField(max_length=64, default="Not considered")

    def accept(self):
        self.is_accepted = True
        self.status = "Accepted"
        self.save()

    def deny(self):
        self.is_denied = True
        self.status = "Denied"
        self.save()


class RequestRoleToActor(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    is_denied = models.BooleanField(default=False)
    status = models.CharField(max_length=64, default="Not considered")

    def accept(self):
        self.is_accepted = True
        self.status = "Accepted"
        self.save()

    def deny(self):
        self.is_denied = True
        self.status = "Denied"
        self.save()
