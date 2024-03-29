# Generated by Django 4.2.6 on 2023-12-11 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("malfunctions", "0009_alter_modelmalfunctions_date_time_accepted"),
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
                    21,
                    37,
                    6,
                    230995,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="status",
            field=models.BooleanField(
                default="True", verbose_name="Статус заявки"
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="transfer_of_the_application",
            field=models.BooleanField(
                default="False", verbose_name="Передача по смене"
            ),
        ),
    ]
