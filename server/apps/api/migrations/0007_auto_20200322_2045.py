# Generated by Django 3.0.4 on 2020-03-22 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200321_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='clothesset',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='clothessetreview',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='clothesset',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='clothesset',
            name='style',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
