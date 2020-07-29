from django.db import models
from contact.models import Contact, Company
from project.models import Project
from document.models import Contract, Document

class ContractPlan(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название плана")
    contract = models.ForeignKey(Contract, verbose_name="Договор / ДС", blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Календарный план"
        verbose_name_plural = "Календарные планы"
        ordering = ['name', 'contract']

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="Проект")
    num = models.CharField(max_length=20, verbose_name="Номер в календарном плане", blank=True)
    contract_plan = models.ForeignKey(ContractPlan, verbose_name="Календарный план", blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, verbose_name="Задача")
    info = models.TextField(verbose_name="Описание", blank=True)
    reg_date = models.DateField(verbose_name="Дата создания", blank=True)
    plan_start_date = models.DateField(verbose_name="Дата начала (План)", blank=True)
    actual_start_date = models.DateField(verbose_name="Дата начала (Факт)", blank=True)
    plan_end_date = models.DateField(verbose_name="Дата завершения (План)", blank=True)
    actual_end_date = models.DateField(verbose_name="Дата завершения (Факт)", blank=True)
    end_report = models.TextField(verbose_name="Отчет о завершении", blank=True)
    exec_companies = models.ManyToManyField(Company, verbose_name="Исполнитель (Компания)", blank=True)
    exec_contacts = models.ManyToManyField(Contact, verbose_name="Исполнитель", blank=True)
    documents = models.ManyToManyField(Document, verbose_name="Отчетные документы", blank=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ['contract_plan', 'num', 'plan_start_date', 'name']

    def __str__(self):
        return self.name


class TaskComment(models.Model):
    task = models.ForeignKey(Task, verbose_name="Задача", on_delete=models.PROTECT)
    comment = models.TextField(verbose_name="Комментарий")
    comment_date = models.DateField(verbose_name="Дата комментария")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['task', 'comment_date']

    def __str__(self):
        return self.comment
