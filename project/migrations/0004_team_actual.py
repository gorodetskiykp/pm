# Generated by Django 3.0.8 on 2020-07-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_role_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='actual',
            field=models.BooleanField(default=True, verbose_name='В проекте (актуальность)'),
        ),
    ]