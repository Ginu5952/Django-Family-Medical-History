# Generated by Django 5.0.6 on 2024-07-06 14:39

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("hospitalDetails", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("department", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="DoctorDetail",
            fields=[
                ("doctor_id", models.AutoField(primary_key=True, serialize=False)),
                ("doctor_name", models.CharField(max_length=20)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "availability_days",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=20),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "consultation_hours",
                    models.JSONField(blank=True, default=list, null=True),
                ),
                ("contact_no", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "departments",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctors",
                        to="doctorDetails.department",
                    ),
                ),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospitalDetails.hospitaldetail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DoctorDepartment",
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
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctorDetails.doctordetail",
                    ),
                ),
            ],
        ),
    ]
