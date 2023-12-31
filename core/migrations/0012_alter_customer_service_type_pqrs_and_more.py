# Generated by Django 4.2.4 on 2023-09-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rendezvous_respondido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_service',
            name='type_pqrs',
            field=models.CharField(choices=[('Reclamo', 'Reclamo'), ('Peticion', 'Peticion'), ('Queja', 'Queja'), ('Sugerencia', 'Sugerencia')], max_length=100, verbose_name='Tipo PQRS'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='appointment_type',
            field=models.CharField(choices=[('Consulta', 'Consulta'), ('Seguimiento', 'Seguimiento'), ('Primera Vez', 'Primera Vez')], max_length=100, verbose_name='Tipo de cita'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(choices=[('Tarjeta ', 'Tarjeta '), ('Efectivo', 'Efectivo')], max_length=100, verbose_name='Metodo de pago'),
        ),
    ]
