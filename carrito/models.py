from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(unique=True,max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    inventario = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.descripcion} {self.precio} {self.inventario}"

class Carrito(models.Model):
    name = models.CharField(max_length=128)
    productos = models.ManyToManyField(Producto, through="ItemCarrito")

    def __str__(self):
        return self.name

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Customer(models.Model):
    document_number = models.CharField(unique=True, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    residence_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.document_number} {self.first_name} {self.last_name}"