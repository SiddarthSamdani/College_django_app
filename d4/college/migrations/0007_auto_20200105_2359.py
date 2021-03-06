# Generated by Django 2.2.6 on 2020-01-05 18:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0006_auto_20200105_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myimg',
            field=models.ImageField(null=True, upload_to='images\\'),
        ),
        migrations.AddField(
            model_name='profile',
            name='myresume',
            field=models.FileField(null=True, upload_to='doc\\'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marks_10',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marks_12',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='marks_aggr',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
