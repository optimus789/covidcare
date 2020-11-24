# Generated by Django 3.0.2 on 2020-04-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidManager', '0006_covidiot_iv'),
    ]

    operations = [
        migrations.AddField(
            model_name='covidiot',
            name='appetite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='covidiot',
            name='breathlessness',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='covidiot',
            name='cough',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='covidiot',
            name='smell',
            field=models.BooleanField(default=False),
        ),
    ]