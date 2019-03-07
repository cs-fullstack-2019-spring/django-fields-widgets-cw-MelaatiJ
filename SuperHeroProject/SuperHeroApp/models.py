from django.db import models


# Create your models here.

# super hero model with quetions for form
class SuperHeroModel(models.Model):
    name = models.CharField(max_length=200)
    fromWhere = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    intention = models.CharField(max_length=100)
    examples = models.TextField()

    def __str__(self):
        return self.name
