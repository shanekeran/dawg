# Generated by Django 3.2.4 on 2021-09-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='store_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
