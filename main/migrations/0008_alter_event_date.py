# Generated by Django 4.0.1 on 2022-01-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
