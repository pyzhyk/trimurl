# Generated by Django 3.2.12 on 2022-07-13 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0004_shortener'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shortener',
        ),
    ]