# Generated by Django 3.0.5 on 2020-05-03 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200503_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='updated_datatime',
            new_name='updated_datetime',
        ),
    ]
