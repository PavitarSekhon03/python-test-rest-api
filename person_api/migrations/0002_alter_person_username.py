# Generated by Django 4.2.9 on 2024-01-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
