# Generated by Django 5.0 on 2024-07-13 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admRrhh', '0005_alter_personal_fechvenlic_perl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='tipoLic_perl',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Tipo de Licencia'),
        ),
    ]