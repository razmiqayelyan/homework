# Generated by Django 3.1.7 on 2021-04-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='surname',
        ),
        migrations.AddField(
            model_name='booking',
            name='employer',
            field=models.CharField(max_length=50, null=True, verbose_name='Who do you want to book with?'),
        ),
    ]
