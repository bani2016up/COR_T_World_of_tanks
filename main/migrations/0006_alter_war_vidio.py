# Generated by Django 4.0.1 on 2022-01-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_war_vidio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='war',
            name='vidio',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
