from django.db import models

class Fila(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
