from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from .elo import Elo
from .modalidade import Modalidade
from .fila import Fila
from .status import Status
from datetime import datetime


class Servico(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=False)
    # current_elo = models.ForeignKey(Elo, related_name="servicos_iniciais", on_delete=models.PROTECT, null=False)
    # target_elo = models.ForeignKey(Elo, related_name="servicos_finais", on_delete=models.PROTECT, null=False)
    # queue = models.ForeignKey(Fila, on_delete=models.PROTECT, null=False)
    # service = models.ForeignKey(Modalidade, on_delete=models.PROTECT, related_name="servicos_type", default=1, null=False)
    # status = models.ForeignKey(Status, related_name="servicos_status", on_delete=models.PROTECT, default=1, null=False)

    # Novos campos adicionados
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, default=1)
    service = models.ForeignKey(
        Modalidade, on_delete=models.PROTECT, related_name="servicos_type", default=1, null=True
    )
    queue = models.ForeignKey(Fila, on_delete=models.PROTECT, null=True, default=1)
    status = models.ForeignKey(Status, related_name="servicos_status", on_delete=models.PROTECT, null=True, default=1)
    current_elo = models.CharField(max_length=50, null=True)
    target_elo = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=500, null=True)
    riot_login = models.CharField(max_length=50, null=True)
    riot_password = models.CharField(max_length=50, null=True)
    refer_code = models.CharField(max_length=50, null=True)
    payment_method = models.CharField(max_length=50, null=True, default="Pix")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    riot_id = models.CharField(max_length=50, null=True)
    riot_tag = models.CharField(max_length=50, null=True, default="#BR1")
    time = models.IntegerField(null=True)

    def __str__(self):
        current_elo_name = self.current_elo.nome if isinstance(self.current_elo, Elo) else self.current_elo
        target_elo_name = self.target_elo.nome if isinstance(self.target_elo, Elo) else self.target_elo
        username = self.user.username if self.user else "N/A"  # Se não houver usuário, exiba "N/A"

        return (
            f"{current_elo_name} ao {target_elo_name} - {self.user.email} - {self.status} - prazo de {self.time} dias"
        )

    #   return f"{self.current_elo} ao {self.target_elo} - {self.user.username} - {self.status} - prazo de {self.time} dias"

    # def clean(self):
    #     if self.current_elo >= self.target_elo:
    #         raise ValidationError("O elo final deve ser maior que o elo inicial.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Servico, self).save(*args, **kwargs)
