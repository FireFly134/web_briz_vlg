from django.db import models

from main.models import (
    AddressList,
    DispatcherList,
    MechanicsList,
)


# Заявки
class ModelMalfunctions(models.Model):
    address = models.ForeignKey(AddressList, on_delete=models.CASCADE)
    num_house = models.CharField(
        verbose_name="Номер дома",
    )
    entrance = models.CharField(
        verbose_name="Подъезд",
    )
    flat_or_tel = models.CharField(
        verbose_name="Номер квартины или телефона",
    )
    dispatcher = models.ForeignKey(DispatcherList, on_delete=models.CASCADE)
    date_time_accepted = models.DateTimeField(
        verbose_name="Дата приема заявки",
        null=True,
    )
    mechanics = models.ManyToManyField(
        MechanicsList,
        related_name="mechanics",
        default=None,
    )
    date_time_transfer = models.DateTimeField(
        verbose_name="Дата передачи заявки механикам",
        null=True,
    )
    malfunction_and_cause = models.CharField(
        verbose_name="Неисправность и причина заявки",
        null=True,
    )
    date_time_closed = models.DateTimeField(
        verbose_name="Дата закрытия заявки",
        null=True,
    )
    simple = models.CharField(verbose_name="Простой", null=True, default="")
    executor_mechanics = models.ManyToManyField(
        MechanicsList,
        related_name="executor_mechanics",
        default=None,
    )
    description = models.CharField(
        verbose_name="Примечания",
        null=True,
    )
    status = models.BooleanField(
        verbose_name="Статус заявки",
        default=True,
    )

    def __str__(self) -> str:
        return f"{self.address} - {self.entrance}"

    class Meta:
        verbose_name = "сервисная заявка"
        verbose_name_plural = "сервесные заявки"
        # ordering = ['']
