# Generated by Django 5.1.3 on 2024-11-21 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_entry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]