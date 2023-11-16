from django.core.exceptions import ValidationError
from django.db import models
from .elo import Elo
from .modalidade import Modalidade
from .fila import Fila
from django.contrib.auth.models import User
from datetime import datetime

class Servico(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateField(default=datetime.now)
    purchase_time = models.TimeField(default=datetime.now)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE, related_name='servicos')
    fila = models.ForeignKey(Fila, on_delete=models.CASCADE)
    elo_inicial = models.ForeignKey(Elo, related_name='servicos_iniciais', on_delete=models.CASCADE)
    elo_final = models.ForeignKey(Elo, related_name='servicos_finais', on_delete=models.CASCADE)

    def __str__(self):
        if self.completed:
            status = "Finalizado"
        else:
            status = "Em andamento"
        
        formatted_purchase_date = self.purchase_date.strftime("%Y-%m-%d %H:%M:%S")
        formatted_deadline = self.deadline.strftime("%Y-%m-%d %H:%M:%S")
        
        return f"{self.elo_inicial} ao {self.elo_final} - {self.user.username} - {status} até {self.deadline}"

    def clean(self):
        if self.elo_inicial.id >= self.elo_final.id:
            raise ValidationError("O elo final deve ser maior que o elo inicial.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Servico, self).save(*args, **kwargs)
