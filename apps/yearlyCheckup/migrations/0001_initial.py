# Generated by Django 5.0.6 on 2024-07-06 20:37

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("healthInsurance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="YearlyCheckUp",
            fields=[
                (
                    "yearly_check_up_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("yearly_check_up_done", models.BooleanField(default=False)),
                ("date_of_check_up", models.DateField(blank=True, null=True)),
                (
                    "health_insurance_card_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthInsurance.healthinsurancecard",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="yearlycheckup",
            constraint=models.CheckConstraint(
                check=models.Q(("yearly_check_up_done__in", [True, False])),
                name="check_yearly_check_up_done_valid",
            ),
        ),
        migrations.AddConstraint(
            model_name="yearlycheckup",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("date_of_check_up__isnull", True),
                    ("date_of_check_up__lte", datetime.date(2024, 7, 6)),
                    _connector="OR",
                ),
                name="check_date_of_check_up_valid",
            ),
        ),
        migrations.AddConstraint(
            model_name="yearlycheckup",
            constraint=models.UniqueConstraint(
                fields=("health_insurance_card_no", "date_of_check_up"),
                name="unique_health_insurance_card_date_of_check_up",
            ),
        ),
    ]
