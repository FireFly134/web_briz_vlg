# Generated by Django 4.2.6 on 2023-12-10 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "malfunctions",
            "0002_remove_modelmalfunctions_date_time_closed_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modelmalfunctions",
            name="date_closed",
        ),
        migrations.RemoveField(
            model_name="modelmalfunctions",
            name="time_closed",
        ),
        migrations.AddField(
            model_name="modelmalfunctions",
            name="date_time_closed",
            field=models.DateField(
                default=datetime.datetime(
                    2023,
                    12,
                    10,
                    22,
                    45,
                    11,
                    780364,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата закрытия заявки",
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateField(
                default=datetime.datetime(
                    2023,
                    12,
                    10,
                    22,
                    45,
                    11,
                    780295,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
    ]