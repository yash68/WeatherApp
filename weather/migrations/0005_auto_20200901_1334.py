# Generated by Django 3.1 on 2020-09-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20200901_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='flag',
            field=models.IntegerField(default=0),
        ),
    ]