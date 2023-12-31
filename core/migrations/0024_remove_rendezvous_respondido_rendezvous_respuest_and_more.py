# Generated by Django 4.2.4 on 2023-10-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_customer_service_prioridad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rendezvous',
            name='respondido',
        ),
        migrations.AddField(
            model_name='rendezvous',
            name='respuest',
            field=models.CharField(choices=[('NO RESPONDIDO', 'NO RESPONDIDO'), ('RESPONDIDO', 'RESPONDIDO')], default='', max_length=100, verbose_name='Respuesta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer_service',
            name='Priority',
            field=models.CharField(choices=[('Media', 'Media'), ('Baja', 'Baja'), ('Alta', 'Alta')], max_length=100, verbose_name='Prioridad PQRS'),
        ),
        migrations.AlterField(
            model_name='customer_service',
            name='type_pqrs',
            field=models.CharField(choices=[('Peticion', 'Peticion'), ('Sugerencia', 'Sugerencia'), ('Reclamo', 'Reclamo'), ('Queja', 'Queja')], max_length=100, verbose_name='Tipo PQRS'),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='location',
            field=models.CharField(choices=[('Calle 31a #16-23', 'Calle 31a #16-23'), ('VIRTUAL', 'VIRTUAL')], max_length=100, verbose_name='Ubicacion'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='payment_method',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Tarjeta ', 'Tarjeta ')], max_length=100, verbose_name='Metodo de pago'),
        ),
    ]
