from django.db import models
from contact.models import Contact

class Project(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Имя проекта")
    abbr_name = models.CharField(max_length=20, verbose_name="Аббревиатура проекта")
    upit_code = models.CharField(max_length=10, verbose_name="КОД УПИТ", default="PR_")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['abbr_name']

    def __str__(self):
        return f"{self.abbr_name} [{self.upit_code}]"


class Role(models.Model):
    role = models.CharField(max_length=100, verbose_name="Роль в проекте")

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
        ordering = ['role']

    def __str__(self):
        return self.role


class Team(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, verbose_name="Проект")
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Роль")
    team_name = models.CharField(max_length=100, verbose_name="Название команды", blank=True)
    name = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name="Имя")
    actual = models.BooleanField(default=True, verbose_name="В проекте (актуальность)")
    info = models.CharField(max_length=500, verbose_name="Зона ответственности, задачи", blank=True)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ['project', 'team_name', 'name', 'role']

    def __str__(self):
        return f"{self.project}, {self.team_name}, {self.role}, {self.name}"
