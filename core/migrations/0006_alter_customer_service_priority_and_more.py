# Generated by Django 4.2.4 on 2023-09-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customer_service_priority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_service',
            name='priority',
            field=models.CharField(choices=[('Media', 'Media'), ('Baja', 'Baja'), ('Alta', 'Alta')], max_length=100, verbose_name='Prioridad PQRS'),
        ),
        migrations.AlterField(
            model_name='customer_service',
            name='type_pqrs',
            field=models.CharField(choices=[('Sugerencia', 'Sugerencia'), ('Queja', 'Queja'), ('Peticion', 'Peticion'), ('Reclamo', 'Reclamo')], max_length=100, verbose_name='Tipo PQRS'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='appointment_type',
            field=models.CharField(choices=[('Seguimiento', 'Seguimiento'), ('Primera Vez', 'Primera Vez'), ('Consulta', 'Consulta')], max_length=100, verbose_name='Tipo de cita'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='virtual_onsite',
            field=models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual')], max_length=100, verbose_name='Virtual o presencial'),
        ),
    ]
