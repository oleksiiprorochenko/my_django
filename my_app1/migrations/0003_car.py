# Generated by Django 5.0.1 on 2024-01-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0002_person_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4)),
                ('car_name', models.CharField(max_length=30)),
            ],
        ),
    ]
