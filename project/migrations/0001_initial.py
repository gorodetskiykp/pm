# Generated by Django 3.0.8 on 2020-07-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Имя проекта')),
                ('abbr_name', models.CharField(max_length=20, verbose_name='Аббревиатура проекта')),
                ('upit_code', models.CharField(default='PR_', max_length=10, verbose_name='КОД УПИТ')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
