# Generated by Django 5.0.4 on 2024-04-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cymbal',
            name='size',
            field=models.IntegerField(),
        ),
    ]
