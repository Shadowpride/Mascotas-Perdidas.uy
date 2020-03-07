from django.db import models




'''class Estado(models.Model):
    situacion = models.CharField(max_length=40)  # <---- Para indicar si esta perdido o encontrado

    def __str__(self):
        return self.situacion'''


class Barrio(models.Model):
    lugar = models.CharField(max_length=40)  # <---- Para indicar el barrio donde se perdio

    def __str__(self):
        return self.lugar


class Tipo(models.Model):
    especie = models.CharField(max_length=40)  # <---- Para indicar si es perro, gato, etc.

    def __str__(self):
        return self.especie


class Raza(models.Model):
    tipo = models.CharField(max_length=40)  # <---- Para indicar la raza del animal

    def __str__(self):
        return self.tipo


class MascotaPerdida(models.Model):
    estado = models.CharField(max_length=40)
    imagen = models.ImageField(null=True, blank=True)  # <---- NO SACAR EL NULL NI EL BLANK QUE SE ROMPE LA BBDD
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)

    fecha = models.DateField()
    nombre = models.CharField(max_length=40)
    mail = models.EmailField()
    telefono = models.IntegerField()
    descripcion = models.TextField()





