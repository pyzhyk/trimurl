# Generated by Django 3.2.12 on 2022-07-13 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0002_remove_shortener_times_followed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shortener',
        ),
    ]