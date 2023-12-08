# adicionar_elos.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from core.models import Elo

# Lista de elos
elos = [
    "Ferro 4",
    "Ferro 3",
    "Ferro 2",
    "Ferro 1",
    "Bronze 4",
    "Bronze 3",
    "Bronze 2",
    "Bronze 1",
    "Prata 4",
    "Prata 3",
    "Prata 2",
    "Prata 1",
    "Ouro 4",
    "Ouro 3",
    "Ouro 2",
    "Ouro 1",
    "Platina 4",
    "Platina 3",
    "Platina 2",
    "Platina 1",
    "Esmeralda 4",
    "Esmeralda 3",
    "Esmeralda 2",
    "Esmeralda 1",
    "Diamante 4",
    "Diamante 3",
    "Diamante 2",
    "Diamante 1",
    "Mestre",
    "Grão Mestre",
    "Desafiante",
]

# Adiciona os elos ao banco de dados
for elo_name in elos:
    elo, created = Elo.objects.get_or_create(name=elo_name)
    if created:
        print(f'Elo "{elo_name}" criado com sucesso.')
    else:
        print(f'Elo "{elo_name}" já existe.')
