# Generated by Django 4.0.4 on 2022-04-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_projectdev'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdev',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
