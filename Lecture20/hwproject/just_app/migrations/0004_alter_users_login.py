# Generated by Django 4.1.5 on 2023-01-07 17:45

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ("just_app", "0003_alter_users_login"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="login",
            field=models.CharField(
                max_length=25,
                validators=[
                    django.core.validators.RegexValidator(
                        code="",
                        flags=re.RegexFlag["IGNORECASE"],
                        inverse_match=False,
                        message="He корректно введен логин!",
                        regex="(?=\\d*)(?=[a-z]*)(?=[A-Z]*).{6,25}$",
                    )
                ],
                verbose_name="login",
            ),
        ),
    ]