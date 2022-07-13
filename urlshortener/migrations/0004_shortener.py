# Generated by Django 3.2.12 on 2022-07-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('urlshortener', '0003_delete_shortener'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('long_url', models.URLField()),
                ('short_url', models.CharField(blank=True, max_length=15, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
