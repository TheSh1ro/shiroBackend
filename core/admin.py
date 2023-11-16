from django.contrib import admin
from core.models import Servico, Fila, Modalidade, Elo, Status

admin.site.register(Servico)
admin.site.register(Fila)
admin.site.register(Modalidade)
admin.site.register(Elo)
admin.site.register(Status)
