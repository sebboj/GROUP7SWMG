# Generated by Django 4.2.7 on 2023-11-03 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]