from django.db import models
from django.utils.timezone import now

from main.models import (
    AddressList,
    DispatcherList,
    MechanicsList,
)


# Заявки
class ModelMalfunctions(models.Model):
    address = models.ForeignKey(
        AddressList, on_delete=models.CASCADE
    )
    entrance = models.CharField(
        verbose_name="Подъезд",
    )
    flat_or_tel = models.CharField(
        verbose_name="Номер квартины или телефона",
    )
    dispatcher = models.ForeignKey(
        DispatcherList, on_delete=models.CASCADE
    )
    date_time_accepted = models.DateField(
        verbose_name="Дата приема заявки",
        default=now(),
    )
    mechanics = models.ForeignKey(
        MechanicsList, on_delete=models.CASCADE,
        related_name='mechanics',
        default=None
    )
    date_time_closed = models.DateField(
        verbose_name="Дата закрытия заявки",
        default=now(),
    )
    malfunction_and_cause = models.CharField(
        verbose_name="Неисправность и причина заявки",
    )
    transfer_of_the_application = models.BooleanField(
        verbose_name="Передача по смене",
        default=False,
    )
    executor_mechanics = models.ForeignKey(
        MechanicsList, on_delete=models.CASCADE,
        related_name='executor_mechanics',
        default=None
    )
    description = models.CharField(
        verbose_name="Примечания",
    )

    def __str__(self) -> str:
        return f"{self.address} - {self.entrance}"

    class Meta:
        verbose_name = "сервисная заявка"
        verbose_name_plural = "сервесные заявки"
        # ordering = ['']
