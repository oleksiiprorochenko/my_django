# Generated by Django 5.0.1 on 2024-01-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]
