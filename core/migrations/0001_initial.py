# Generated by Django 4.2.4 on 2023-09-18 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date_pqrs', models.DateField(blank=True, null=True, verbose_name='Fecha solicitud PQRS')),
                ('number_phone', models.CharField(max_length=10, verbose_name='Numero Telefonico')),
                ('type_pqrs', models.CharField(choices=[('Peticion', 'Peticion'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Sugerencia', 'Sugerencia')], max_length=100, verbose_name='Tipo PQRS')),
                ('priority', models.CharField(choices=[('Media', 'Media'), ('Alta', 'Alta'), ('Baja', 'Baja')], max_length=100, verbose_name='Prioridad PQRS')),
                ('description', models.TextField(max_length=2000, verbose_name='Descripcion PQRS')),
            ],
            options={
                'verbose_name': 'Atencion cliente',
                'verbose_name_plural': 'Atencion Clientes',
                'db_table': 'Atencion cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order', models.FloatField(verbose_name='Orden de compra')),
                ('quantity_products', models.FloatField(verbose_name='Cantidad productos')),
                ('existing_products', models.FloatField(verbose_name='Productos existentes')),
                ('batches_products', models.FloatField(verbose_name='Numero lotes de productos')),
                ('expiration_date', models.DateField(verbose_name='Fecha vencimiento')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'Inventario',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('expiration_date', models.DateField(verbose_name='Fecha vencimiento')),
                ('serial_number', models.FloatField(verbose_name='Número de serie')),
                ('weight', models.FloatField(verbose_name='Gramaje')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
                ('type_presentation', models.CharField(max_length=80, verbose_name='Tipo de presentación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'Producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Rendezvous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='Fecha de Cita')),
                ('email', models.CharField(max_length=100, verbose_name='Correo electronico')),
                ('virtual_onsite', models.CharField(choices=[('Presencial', 'Presencial'), ('Virtual', 'Virtual')], max_length=100, verbose_name='Virtual o presencial')),
                ('location', models.CharField(choices=[('Calle 31a #16-23', 'Calle 31a #16-23')], max_length=100, verbose_name='Ubicacion')),
                ('appointment_type', models.CharField(choices=[('Consulta', 'Consulta'), ('Seguimiento', 'Seguimiento'), ('Primera Vez', 'Primera Vez')], max_length=100, verbose_name='Tipo de cita')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': 'Cita',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sale', models.DateField(verbose_name='Fecha de venta')),
                ('payment_method', models.CharField(max_length=100, verbose_name='Metodo de pago')),
                ('coupons_available', models.FloatField(verbose_name='Cupones disponibles')),
                ('receipt_number', models.FloatField(verbose_name='Numero de recibo')),
                ('unit_value', models.FloatField(verbose_name='Valor unitario')),
                ('total_value', models.FloatField(verbose_name='Valor total')),
                ('quantity', models.FloatField(verbose_name='Cantidad')),
                ('order_number', models.FloatField(verbose_name='Numero de orden')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'Venta',
                'ordering': ['id'],
            },
        ),
    ]
