# Generated by Django 2.2.6 on 2020-01-05 18:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_profile_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='marks_10',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='marks_12',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='marks_aggr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='profile',
            name='pn',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
