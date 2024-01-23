# Generated by Django 4.2.6 on 2024-01-06 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_routers_emai_alter_simcard_ip"),
        ("malfunctions", "0015_alter_modelmalfunctions_date_time_accepted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 1, 6, 17, 19, 6, 55241, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
        migrations.RemoveField(
            model_name="modelmalfunctions",
            name="executor_mechanics",
        ),
        migrations.RemoveField(
            model_name="modelmalfunctions",
            name="mechanics",
        ),
        migrations.AddField(
            model_name="modelmalfunctions",
            name="executor_mechanics",
            field=models.ManyToManyField(
                default=None,
                related_name="executor_mechanics",
                to="main.mechanicslist",
            ),
        ),
        migrations.AddField(
            model_name="modelmalfunctions",
            name="mechanics",
            field=models.ManyToManyField(
                default=None, related_name="mechanics", to="main.mechanicslist"
            ),
        ),
    ]