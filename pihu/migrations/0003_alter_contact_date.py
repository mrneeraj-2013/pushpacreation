# Generated by Django 4.2.3 on 2023-07-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pihu', '0002_rename_contact_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
