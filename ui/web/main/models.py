from django.db import models


# Список адресов
class AddressList(models.Model):
    address = models.CharField(
        verbose_name="Адрес",
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.address)

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "Список адресов"


# Список диспетчеров
class DispatcherList(models.Model):
    fio = models.CharField(
        max_length=200,
        verbose_name="ФИО диспетчера",
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "диспетчера"
        verbose_name_plural = "Список диспетчеров"


# Список механиков
class MechanicsList(models.Model):
    fio = models.CharField(
        max_length=200,
        verbose_name="ФИО механика",
        unique=True,
    )

    def __str__(self) -> str:
        return str(self.fio)

    class Meta:
        verbose_name = "механика"
        verbose_name_plural = "Список механиков"


# Список СимКарт
class SimCard(models.Model):
    phone_number = models.CharField(
        max_length=12,
        null=False,
        verbose_name="Номер телефона",
        blank=True,
        unique=True,
    )
    ip = models.CharField(
        max_length=15,
        verbose_name="IP симкарты",
        blank=True,
    )
    operator_name = models.CharField(
        null=False, verbose_name="Наименование оператора"
    )

    def __str__(self) -> str:
        return str(self.ip)

    class Meta:
        verbose_name = "симку"
        verbose_name_plural = "Список симкарт"


# Список механиков
class Routers(models.Model):
    name_router = models.CharField(
        null=False,
        verbose_name="Название роутера",
        blank=True,
    )
    emai = models.CharField(verbose_name="Номер роутера")
    imei = models.CharField(verbose_name="IMEI роутера", null=True)

    info_install = models.CharField(
        verbose_name="Доп. информация", blank=True, default=""
    )

    def __str__(self) -> str:
        return str(self.imei)

    class Meta:
        verbose_name = "роутер"
        verbose_name_plural = "Список роутеров"
