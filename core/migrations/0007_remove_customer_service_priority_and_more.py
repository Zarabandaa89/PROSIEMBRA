# Generated by Django 4.2.4 on 2023-09-23 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_customer_service_priority_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_service',
            name='priority',
        ),
        migrations.AlterField(
            model_name='customer_service',
            name='type_pqrs',
            field=models.CharField(choices=[('Queja', 'Queja'), ('Peticion', 'Peticion'), ('Reclamo', 'Reclamo'), ('Sugerencia', 'Sugerencia')], max_length=100, verbose_name='Tipo PQRS'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='virtual_onsite',
            field=models.CharField(choices=[('Virtual', 'Virtual'), ('Presencial', 'Presencial')], max_length=100, verbose_name='Virtual o presencial'),
        ),
    ]
