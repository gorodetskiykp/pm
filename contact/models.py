from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    short_name = models.CharField(max_length=100, verbose_name="Сокращённое название")

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"
        ordering = ['short_name']

    def __str__(self):
        return self.short_name


class Phone(models.Model):
    phone_number = models.CharField(max_length=100, verbose_name="Номер")
    comment = models.CharField(max_length=100, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Телефон"
        verbose_name_plural = "Телефоны"
        ordering = ['phone_number']

    def __str__(self):
        return self.phone_number


class Email(models.Model):
    email = models.CharField(max_length=100, verbose_name="Адрес электронной почты")

    class Meta:
        verbose_name = "Адрес электронной почты"
        verbose_name_plural = "Адреса электронной почты"
        ordering = ['email']

    def __str__(self):
        return self.email


class Skype(models.Model):
    skype = models.CharField(max_length=100, verbose_name="Skype-логин")

    class Meta:
        verbose_name = "Skype-логин"
        verbose_name_plural = "Skype-логины"
        ordering = ['skype']

    def __str__(self):
        return self.skype


class Contact(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    second_name = models.CharField(max_length=100, verbose_name="Отчество")
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Компания")
    post = models.CharField(max_length=100, verbose_name="Должность")
    phones = models.ManyToManyField(Phone, verbose_name="Телефоны")
    emails = models.ManyToManyField(Email, verbose_name="Адреса электронной почты")
    skypes = models.ManyToManyField(Skype, verbose_name="Skype-логины")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}.{self.second_name[0]}."
