# Generated by Django 4.2.6 on 2023-12-11 23:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("malfunctions", "0012_alter_modelmalfunctions_date_time_accepted"),
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
                    23,
                    21,
                    39,
                    810616,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
    ]
