# Generated by Django 3.0.5 on 2020-05-03 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200503_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_datatime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
