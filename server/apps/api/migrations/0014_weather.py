# Generated by Django 3.0.4 on 2020-04-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20200402_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_code', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.IntegerField(choices=[(2, 2), (5, 5), (8, 8), (11, 11), (14, 14), (17, 17), (20, 20), (23, 23)])),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_sensible_temp', models.FloatField()),
                ('min_sensible_temp', models.FloatField()),
                ('humidity', models.IntegerField()),
                ('wind_speed', models.FloatField()),
                ('precipitation', models.IntegerField()),
            ],
        ),
    ]
