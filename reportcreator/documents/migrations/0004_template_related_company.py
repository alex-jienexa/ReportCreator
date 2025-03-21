# Generated by Django 5.1.6 on 2025-03-21 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('documents', '0003_remove_template_variables_template_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='related_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='companies.contractor', verbose_name='Связанная компания'),
        ),
    ]
