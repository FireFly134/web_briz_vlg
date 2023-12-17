from django.db import models


# Список адресов
class AddressList(models.Model):
    address = models.CharField(verbose_name="Адрес")

    def __str__(self) -> str:
        return str(self.address)

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "Список адресов"


# Список диспетчеров
class DispatcherList(models.Model):
    fio = models.CharField(max_length=200, verbose_name="ФИО диспетчера")

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "диспетчера"
        verbose_name_plural = "Список диспетчеров"


# Список механиков
class MechanicsList(models.Model):
    fio = models.CharField(max_length=200, verbose_name="ФИО механика")

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "механика"
        verbose_name_plural = "Список механиков"


# Список СимКарт
class SimCard(models.Model):
    phone_number = models.CharField(
        max_length=10,
        null=False,
        verbose_name="Номер телефона",
    )
    ip = models.CharField(max_length=12, verbose_name="IP симкарты")
    operator_name = models.CharField(
        null=False,
        verbose_name="Наименование оператора")

    def __str__(self) -> str:
        return str(self.ip)

    class Meta:
        verbose_name = "симку"
        verbose_name_plural = "Список симкарт"


# Список механиков
class Routers(models.Model):
    name_router = models.CharField(
        null=False,
        verbose_name="Название роутера"
    )
    emai = models.CharField(
        verbose_name="номер роутера"
    )

    def __str__(self) -> str:
        return str(self.emai)

    class Meta:
        verbose_name = "роутер"
        verbose_name_plural = "Список роутеров"
