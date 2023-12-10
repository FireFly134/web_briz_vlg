# Generated by Django 4.2.6 on 2023-12-10 23:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "malfunctions",
            "0004_alter_modelmalfunctions_date_time_accepted_and_more",
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
                    10,
                    23,
                    46,
                    11,
                    519767,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_closed",
            field=models.DateTimeField(
                null=True, verbose_name="Дата закрытия заявки"
            ),
        ),
    ]
