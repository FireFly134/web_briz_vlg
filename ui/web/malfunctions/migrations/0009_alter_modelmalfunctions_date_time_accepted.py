# Generated by Django 4.2.6 on 2023-12-11 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "malfunctions",
            "0008_modelmalfunctions_num_house_modelmalfunctions_status_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023,
                    12,
                    11,
                    20,
                    57,
                    24,
                    484922,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
    ]
