# Generated by Django 4.1.7 on 2023-07-06 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agency.agency'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('counselor', 'Counselor')], max_length=20, null=True),
        ),
    ]
