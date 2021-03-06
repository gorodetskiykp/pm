# Generated by Django 3.0.8 on 2020-07-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0005_team_info'),
        ('contact', '0003_auto_20200723_1722'),
        ('document', '0003_auto_20200727_1853'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название плана')),
                ('contract', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='document.Contract', verbose_name='Договор / ДС')),
            ],
            options={
                'verbose_name': 'Календарный план',
                'verbose_name_plural': 'Календарные планы',
                'ordering': ['name', 'contract'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(blank=True, max_length=20, verbose_name='Номер в календарном плане')),
                ('name', models.CharField(max_length=200, verbose_name='Задача')),
                ('info', models.TextField(blank=True, verbose_name='Описание')),
                ('reg_date', models.DateField(blank=True, verbose_name='Дата создания')),
                ('plan_start_date', models.DateField(blank=True, verbose_name='Дата начала (План)')),
                ('actual_start_date', models.DateField(blank=True, verbose_name='Дата начала (Факт)')),
                ('plan_end_date', models.DateField(blank=True, verbose_name='Дата завершения (План)')),
                ('actual_end_date', models.DateField(blank=True, verbose_name='Дата завершения (Факт)')),
                ('end_report', models.TextField(blank=True, verbose_name='Отчет о завершении')),
                ('contract_plan', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='task.ContractPlan', verbose_name='Календарный план')),
                ('exec_companies', models.ManyToManyField(blank=True, to='contact.Company', verbose_name='Исполнитель (Компания)')),
                ('exec_contacts', models.ManyToManyField(blank=True, to='contact.Contact', verbose_name='Исполнитель')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.Project', verbose_name='Проект')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['contract_plan', 'num', 'plan_start_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('plan_end_date', models.DateField(verbose_name='Дата комментария')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task.Task', verbose_name='Задача')),
            ],
        ),
    ]
