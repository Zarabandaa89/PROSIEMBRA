# Generated by Django 4.2.4 on 2023-09-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_customer_service_type_pqrs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_service',
            name='Prioridad',
            field=models.CharField(choices=[('Alta', 'Alta'), ('Baja', 'Baja'), ('Media', 'Media')], default='', max_length=100, verbose_name='Prioridad PQRS'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer_service',
            name='type_pqrs',
            field=models.CharField(choices=[('Peticion', 'Peticion'), ('Reclamo', 'Reclamo'), ('Queja', 'Queja'), ('Sugerencia', 'Sugerencia')], max_length=100, verbose_name='Tipo PQRS'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='virtual_onsite',
            field=models.CharField(choices=[('Virtual', 'Virtual'), ('Presencial', 'Presencial')], max_length=100, verbose_name='Virtual o presencial'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(choices=[('Tarjeta ', 'Tarjeta '), ('Efectivo', 'Efectivo')], max_length=100, verbose_name='Metodo de pago'),
        ),
    ]
