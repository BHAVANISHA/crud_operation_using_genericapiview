# Generated by Django 4.2.4 on 2023-08-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaggerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_detail',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]