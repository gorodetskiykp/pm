from django.db import models
from project.models import Project
from contact.models import Company


class DocumentStatus(models.Model):
    status = models.CharField(max_length=100, verbose_name="Состояние документа")
    status_order = models.PositiveIntegerField(verbose_name="Порядок")

    class Meta:
        verbose_name = "Состояние документа"
        verbose_name_plural = "Состояния документов"
        ordering = ['status_order', 'status']

    def __str__(self):
        return self.status


class Document(models.Model):
    sed_number = models.CharField(max_length=40, verbose_name="Номер СЭД")
    out_number = models.CharField(max_length=40, verbose_name="Внешний номер", blank=True)
    name = models.CharField(max_length=200, verbose_name="Название")
    reg_date = models.DateField(verbose_name="Дата регистрации", blank=True)
    project = models.ForeignKey(Project, verbose_name="Проект", blank=True, on_delete=models.PROTECT, null=True)
    status = models.ForeignKey(DocumentStatus, verbose_name="Состояние документа", blank=True, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ['-reg_date', 'name', 'sed_number']

    def __str__(self):
        return self.name


class Contract(models.Model):
    document = models.ForeignKey(Document, verbose_name="Договор / ДС", on_delete=models.PROTECT)
    additional_agreement = models.PositiveIntegerField(verbose_name="Номер ДС", blank=True)
    document = models.ForeignKey('Contract', verbose_name="Родительский договор (если ДС)", blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Договор / ДС"
        verbose_name_plural = "Договоры / ДС"
        ordering = ['document']

    def __str__(self):
        return self.document.name


class Letter(models.Model):
    document = models.ForeignKey(Document, verbose_name="Письмо", on_delete=models.PROTECT)
    sender = models.ForeignKey(Company, verbose_name="Отправитель", blank=True, on_delete=models.PROTECT, related_name="sender")
    to = models.ForeignKey(Company, verbose_name="Получатель", blank=True, on_delete=models.PROTECT, related_name="to")

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"
        ordering = ['sender', 'to']

    def __str__(self):
        return self.document.name
