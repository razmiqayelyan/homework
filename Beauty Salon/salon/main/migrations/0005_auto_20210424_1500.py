# Generated by Django 3.1.7 on 2021-04-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210424_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_time',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]