# Generated by Django 4.1.7 on 2023-08-03 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_alter_agency_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name': 'Agency', 'verbose_name_plural': 'Agencies'},
        ),
    ]
