from django.db import models


# Список адресов
class AddressList(models.Model):
    address = models.CharField(
        verbose_name="Адрес"
    )

    def __str__(self) -> str:
        return str(self.address)

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "Список адресов"


# Список диспетчеров
class DispatcherList(models.Model):
    fio = models.CharField(
        max_length=200, verbose_name="ФИО диспетчера"
    )

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "диспетчера"
        verbose_name_plural = "Список диспетчеров"


# Список механиков
class MechanicsList(models.Model):
    fio = models.CharField(
        max_length=200, verbose_name="ФИО механика"
    )

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "механика"
        verbose_name_plural = "Список механиков"
