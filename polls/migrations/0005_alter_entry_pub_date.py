# Generated by Django 5.1.3 on 2024-11-22 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
