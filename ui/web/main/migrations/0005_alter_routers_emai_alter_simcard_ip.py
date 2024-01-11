# Generated by Django 4.2.6 on 2024-01-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_routers_simcard"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routers",
            name="emai",
            field=models.CharField(verbose_name="Номер роутера"),
        ),
        migrations.AlterField(
            model_name="simcard",
            name="ip",
            field=models.CharField(max_length=12, verbose_name="IP симкарты"),
        ),
    ]
