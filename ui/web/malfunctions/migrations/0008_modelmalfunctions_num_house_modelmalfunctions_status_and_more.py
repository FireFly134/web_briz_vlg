# Generated by Django 4.2.6 on 2023-12-11 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("malfunctions", "0007_alter_modelmalfunctions_date_time_accepted"),
    ]

    operations = [
        migrations.AddField(
            model_name="modelmalfunctions",
            name="num_house",
            field=models.CharField(default="-", verbose_name="Номер дома"),
        ),
        migrations.AddField(
            model_name="modelmalfunctions",
            name="status",
            field=models.BooleanField(
                default=True, verbose_name="Статус заявки"
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="date_time_accepted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023,
                    12,
                    11,
                    19,
                    45,
                    53,
                    47167,
                    tzinfo=datetime.timezone.utc,
                ),
                verbose_name="Дата приема заявки",
            ),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="description",
            field=models.CharField(null=True, verbose_name="Примечания"),
        ),
        migrations.AlterField(
            model_name="modelmalfunctions",
            name="malfunction_and_cause",
            field=models.CharField(
                null=True, verbose_name="Неисправность и причина заявки"
            ),
        ),
        migrations.DeleteModel(
            name="UpdateModelMalfunctionsForm",
        ),
    ]
