# Generated by Django 5.0.4 on 2024-04-09 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_hire'),
    ]

    operations = [
        migrations.AddField(
            model_name='cymbal',
            name='series',
            field=models.CharField(default='', max_length=20),
        ),
    ]
