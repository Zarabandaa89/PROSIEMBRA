from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Inventory(models.Model):
    purchase_order = models.FloatField(verbose_name= 'Orden de compra')
    quantity_products = models.FloatField(verbose_name= 'Cantidad productos')
    existing_products = models.FloatField(verbose_name= 'Productos existentes')
    batches_products = models.FloatField(verbose_name= 'Numero lotes de productos')
    expiration_date = models.DateField(verbose_name= 'Fecha vencimiento')

    def __str__(self):
        return str(self.purchase_order)
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'Inventario'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    expiration_date = models.DateField(verbose_name='Fecha vencimiento')
    serial_number = models.FloatField(verbose_name='Número de serie')
    weight = models.FloatField(verbose_name='Gramaje') 
    price = models.FloatField(verbose_name='Precio')
    quantity = models.FloatField(verbose_name='Cantidad')
    type_presentation = models.CharField(max_length=80, verbose_name='Tipo de presentación')
    image = models.ImageField(upload_to='products/', null=False, blank=False)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']


class Rendezvous(models.Model):
    #FECHA CITA
    date_time = models.DateTimeField(verbose_name= 'Fecha de Cita')
    
    
   
    email = models.CharField(max_length=100, verbose_name= 'Correo electronico', )
    
    
    #TIPO DE CITA
    
    os_choice = {
        ('Virtual', 'Virtual'),
        ('Presencial', 'Presencial')
    }
    virtual_onsite = models.CharField(max_length=100, verbose_name= 'Virtual o presencial', choices=os_choice)
    
    #UBICACION
    
    os_choice = {
        ('Calle 31a #16-23', 'Calle 31a #16-23'),
        ('VIRTUAL', 'VIRTUAL')
        
    }
    location = models.CharField(max_length=100, verbose_name= 'Ubicacion', choices=os_choice)
    
    #TIPO DE CITA
    os_choice = {
        ('Primera Vez', 'Primera Vez'),
        ('Seguimiento', 'Seguimiento'),
        ('Consulta', 'Consulta'),
    }
    appointment_type = models.CharField( max_length=100, verbose_name= 'Tipo de cita', choices=os_choice)
    
      
    os_choice={
        ('RESPONDIDO', 'RESPONDIDO'),
        ('NO RESPONDIDO', 'NO RESPONDIDO'),
     }
    
    respuest = models.CharField(max_length= 100, verbose_name='Respuesta', choices=os_choice)
    
    
    
    def __str__(self):
        return str(self.date_time)
    
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        db_table = 'Cita'
        ordering = ['id']



class Sale(models.Model):
    date_sale = models.DateField(verbose_name= 'Fecha de venta')
    os_choice = {
        ('Efectivo', 'Efectivo'),
        ('Tarjeta ', 'Tarjeta '),
    }
    payment_method = models.CharField(max_length=100, verbose_name= 'Metodo de pago', choices=os_choice)
    coupons_available = models.FloatField(verbose_name= 'Cupones disponibles')
    receipt_number = models.FloatField(verbose_name= 'Numero de recibo')
    quantity = models.FloatField(verbose_name= 'Cantidad')
    unit_value = models.FloatField(verbose_name= 'Valor unitario')
    total_value = models.FloatField(verbose_name= 'Valor total')
    order_number = models.FloatField(verbose_name= 'Numero de orden')
    
    
    def __str__(self):
        return str(self.date_sale)
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        ordering = ['id']



class Customer_Service(models.Model):
    #FECHA SOLICITUD PQRS
    application_date_pqrs = models.DateField(null=True, blank=True, verbose_name= 'Fecha solicitud PQRS')
    
    
    
    #NUMERO TELEFONICO
    email = models.EmailField(max_length=100, verbose_name= 'Correo electronico', null=True)
    os_choice = {
        ('Reclamo', 'Reclamo'),
        ('Peticion', 'Peticion'),
        ('Sugerencia', 'Sugerencia'),
        ('Queja', 'Queja'),
    }
    
    
    #TIPO PQRS
    type_pqrs = models.CharField(max_length=100, verbose_name= 'Tipo PQRS', choices=os_choice)
    
    #DESCRIPCION
    description = models.TextField(max_length=2000, verbose_name= 'Descripcion PQRS')
    
    os_choice={
        ('RESPONDIDO', 'RESPONDIDO'),
        ('NO RESPONDIDO', 'NO RESPONDIDO'),
     }
    
    respuest = models.CharField(max_length= 100, verbose_name='Respuesta', choices=os_choice)
    
    os_choice={
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    }
    
    Priority= models.CharField(max_length=100, verbose_name='Prioridad PQRS', choices=os_choice)
    

    
    
    def __str__(self):
        return str(self.application_date_pqrs)
    
    class Meta:
        verbose_name = 'Atencion cliente'
        verbose_name_plural = 'Atencion Clientes'
        db_table = 'Atencion cliente'
        ordering = ['id']
        
