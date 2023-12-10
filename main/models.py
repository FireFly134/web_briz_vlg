from django.db import models


# Список адресов
class AddressList(models.Model):
    address = models.CharField(
        max_length=200, verbose_name="Адрес"
    )
    num_house = models.CharField(
        max_length=10, verbose_name="Номер дома"
    )

    def __str__(self) -> str:
        return f"{self.address}, {self.num_house}"

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "Список адресов"


# Список диспетчеров
class DispatcherList(models.Model):
    fio = models.CharField(
        max_length=200, verbose_name="ФИО диспетчера"
    )

    def __str__(self) -> str:
        return f"{self.fio}"

    class Meta:
        verbose_name = "диспетчера"
        verbose_name_plural = "Список диспетчеров"


# Список механиков
class MechanicsList(models.Model):
    fio = models.CharField(
        max_length=200, verbose_name="ФИО механика"
    )

    def __str__(self) -> str:
        return f"{self.fio}"

    class Meta:
        verbose_name = "механика"
        verbose_name_plural = "Список механиков"
