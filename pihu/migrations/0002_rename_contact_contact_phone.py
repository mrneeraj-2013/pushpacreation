# Generated by Django 4.2.3 on 2023-07-26 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pihu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phone',
        ),
    ]