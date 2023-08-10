# Generated by Django 4.1.7 on 2023-08-10 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("agency", "0003_alter_agency_options"),
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="agency",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                to="agency.agency",
            ),
        ),
    ]
