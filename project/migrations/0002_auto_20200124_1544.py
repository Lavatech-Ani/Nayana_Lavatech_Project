# Generated by Django 2.2.7 on 2020-01-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='batchalias',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='batch',
            name='batchid',
            field=models.IntegerField(default=0),
        ),
    ]
