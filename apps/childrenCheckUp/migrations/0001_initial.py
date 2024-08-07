# Generated by Django 5.0.6 on 2024-07-18 20:17

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("familyMember", "0001_initial"),
        ("healthInsurance", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChildrenDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Children Details",
                "db_table": "children_names",
            },
        ),
        migrations.CreateModel(
            name="VaccinationName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "vaccination_name",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "Vaccination Names",
                "db_table": "vaccination_names",
            },
        ),
        migrations.CreateModel(
            name="ChildrenCheckUp",
            fields=[
                ("check_up_id", models.AutoField(primary_key=True, serialize=False)),
                ("number_of_children", models.IntegerField(default=1)),
                ("vaccination_completed", models.BooleanField(default=False)),
                ("date_of_vaccination", models.DateField(blank=True, null=True)),
                (
                    "father_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="father_checkups",
                        to="familyMember.familymember",
                    ),
                ),
                (
                    "health_insurance_card_no",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthInsurance.healthinsurancecard",
                    ),
                ),
                (
                    "mother_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mother_checkups",
                        to="familyMember.familymember",
                    ),
                ),
                (
                    "children_name",
                    models.ManyToManyField(
                        related_name="check_ups", to="childrenCheckUp.childrendetail"
                    ),
                ),
                (
                    "vaccination_name",
                    models.ManyToManyField(
                        blank=True,
                        related_name="children_vaccinations",
                        to="childrenCheckUp.vaccinationname",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Children Vaccination Details",
                "db_table": "children_checkup_details",
            },
        ),
        migrations.AddConstraint(
            model_name="childrencheckup",
            constraint=models.UniqueConstraint(
                fields=("health_insurance_card_no", "father_name", "mother_name"),
                name="unique_checkup_per_family",
            ),
        ),
        migrations.AddConstraint(
            model_name="childrencheckup",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("date_of_vaccination__lte", datetime.date(2024, 7, 18))
                ),
                name="vaccination date cannot be future date",
            ),
        ),
    ]
