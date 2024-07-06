# Generated by Django 5.0.6 on 2024-07-06 15:04

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("doctorDetails", "0002_delete_doctordepartment"),
        ("healthInsurance", "0001_initial"),
        ("hospitalDetails", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FamilyMedicalDetail",
            fields=[
                ("visit_id", models.AutoField(primary_key=True, serialize=False)),
                ("date_of_visit", models.DateField()),
                ("symptoms", models.TextField(blank=True, null=True)),
                ("diagnosis", models.TextField(blank=True, null=True)),
                ("medication", models.TextField(blank=True, null=True)),
                (
                    "department",
                    models.ForeignKey(
                        db_column="department",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctorDetails.department",
                    ),
                ),
                (
                    "doctor_id",
                    models.ForeignKey(
                        db_column="doctor_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_visits",
                        to="doctorDetails.doctordetail",
                    ),
                ),
                (
                    "health_insurance_card_no",
                    models.ForeignKey(
                        db_column="health_insurance_card_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthInsurance.healthinsurancecard",
                    ),
                ),
                (
                    "hospital_id",
                    models.ForeignKey(
                        db_column="hospital_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hospital_visits",
                        to="hospitalDetails.hospitaldetail",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="familymedicaldetail",
            constraint=models.UniqueConstraint(
                fields=(
                    "health_insurance_card_no",
                    "doctor_id",
                    "hospital_id",
                    "department",
                    "date_of_visit",
                ),
                name="unique_doctor_visit",
            ),
        ),
        migrations.AddConstraint(
            model_name="familymedicaldetail",
            constraint=models.CheckConstraint(
                check=models.Q(("date_of_visit__lte", datetime.date(2024, 7, 6))),
                name="Date of visit cannot be future date",
            ),
        ),
    ]
