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


# Сервисные заявки
class ServiceRequests(models.Model):
    name = models.CharField(
        max_length=200, verbose_name="Наименование", db_index=True
    )
    description = models.CharField(
        max_length=200, verbose_name="Описание", db_index=True
    )
    address = models.ForeignKey(
        AddressList, on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        verbose_name="Дата",
    )
    status = models.IntegerField(
        verbose_name="Статус заявки",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "сервисная заявка"
        verbose_name_plural = "Сервисные заявки"
        # ordering = ['']

