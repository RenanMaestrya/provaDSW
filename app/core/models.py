from django.db import models

# Create your models here.
from django.db import models

class City(models.Model):
    name = models.CharField("Nome",max_length=100)
    state = models.CharField("Estado",max_length=2)

    def __str__(self): 
        return self.name
class Course(models.Model):
    name = models.CharField("Nome",max_length=100)

    def __str__(self): 
        return self.name

class Student(models.Model):
    name = models.CharField("Nome",max_length=100)
    email = models.EmailField("Email", max_length=100)
    address = models.CharField("Endereço",max_length=100)
    birthDate = models.DateField("Data de Nascimento")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self): 
        return self.name