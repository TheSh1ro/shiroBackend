from django.core.exceptions import ValidationError
from django.db import models
from .elo import Elo
from .modalidade import Modalidade
from .fila import Fila
from .status import Status
from django.contrib.auth.models import User
from datetime import datetime


class Servico(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    purchase_date = models.DateField(default=datetime.now, null=True)
    purchase_time = models.TimeField(default=datetime.now, null=True)
    deadline = models.DateField(null=False)
    status = models.ForeignKey(Status, related_name="servicos_status", on_delete=models.PROTECT, default=1, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.PROTECT, related_name="servicos", default=1, null=False)
    fila = models.ForeignKey(Fila, on_delete=models.PROTECT, null=False)
    elo_inicial = models.ForeignKey(Elo, related_name="servicos_iniciais", on_delete=models.PROTECT, null=False)
    elo_final = models.ForeignKey(Elo, related_name="servicos_finais", on_delete=models.PROTECT, null=False)

    def __str__(self):
        return f"{self.elo_inicial} ao {self.elo_final} - {self.user.username} - {self.status} - até {self.deadline}"

    def clean(self):
        if self.elo_inicial.id >= self.elo_final.id:
            raise ValidationError("O elo final deve ser maior que o elo inicial.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Servico, self).save(*args, **kwargs)
