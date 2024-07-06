# Generated by Django 5.0.6 on 2024-07-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HospitalDetail",
            fields=[
                ("hospital_id", models.AutoField(primary_key=True, serialize=False)),
                ("hospital_name", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=50)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=15, null=True, unique=True),
                ),
                (
                    "website",
                    models.CharField(blank=True, max_length=25, null=True, unique=True),
                ),
                (
                    "registration_fees",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
            ],
            options={
                "unique_together": {("hospital_name", "location", "address")},
            },
        ),
    ]