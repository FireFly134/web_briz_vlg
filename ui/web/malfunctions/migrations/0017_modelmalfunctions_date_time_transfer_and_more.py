# Generated by Django 4.2.6 on 2024-01-25 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "malfunctions",
            "0016_alter_modelmalfunctions_date_time_accepted_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="modelmalfunctions",
            name="date_time_transfer",
            field=models.DateTimeField(
                null=True, verbose_name="Дата передачи заявки механикам"
            ),
        ),
        migrations.AddField(
            model_name="modelmalfunctions",
            name="simple",
            field=models.CharField(
                default="", null=True, verbose_name="Простой"
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024,
                    1,
                    25,
                    22,
                    10,
                    14,
                    482558,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
    ]
