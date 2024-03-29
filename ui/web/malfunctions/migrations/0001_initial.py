# Generated by Django 4.2.6 on 2023-12-10 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelMalfunctions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entrance", models.CharField(verbose_name="Подъезд")),
                (
                    "flat_or_tel",
                    models.CharField(
                        verbose_name="Номер квартины или телефона"
                    ),
                ),
                (
                    "date_time_accepted",
                    models.DateTimeField(verbose_name="Дата приема заявки"),
                ),
                (
                    "date_time_closed",
                    models.DateTimeField(verbose_name="Дата закрытия заявки"),
                ),
                (
                    "malfunction_and_cause",
                    models.CharField(
                        verbose_name="Неисправность и причина заявки"
                    ),
                ),
                (
                    "transfer_of_the_application",
                    models.BooleanField(verbose_name="Передача по смене"),
                ),
                ("description", models.CharField(verbose_name="Примечания")),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.addresslist",
                    ),
                ),
                (
                    "dispatcher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.dispatcherlist",
                    ),
                ),
                (
                    "mechanics",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.mechanicslist",
                    ),
                ),
            ],
            options={
                "verbose_name": "сервисная заявка",
                "verbose_name_plural": "сервесные заявки",
            },
        ),
        migrations.CreateModel(
            name="UpdateModelMalfunctionsForm",
            fields=[
                (
                    "modelmalfunctions_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="malfunctions.modelmalfunctions",
                    ),
                ),
            ],
            bases=("malfunctions.modelmalfunctions",),
        ),
    ]
