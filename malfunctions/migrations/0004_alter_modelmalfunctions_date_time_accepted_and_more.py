# Generated by Django 4.2.6 on 2023-12-10 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("malfunctions", "0003_remove_modelmalfunctions_date_closed_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateField(
                default=datetime.datetime(
                    2023,
                    12,
                    10,
                    23,
                    42,
                    48,
                    258487,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_closed",
            field=models.DateField(
                default=datetime.datetime(
                    2023,
                    12,
                    10,
                    23,
                    42,
                    48,
                    258583,
                    tzinfo=datetime.timezone.utc,
                ),
                null=True,
                verbose_name="Дата закрытия заявки",
            ),
        ),
    ]
