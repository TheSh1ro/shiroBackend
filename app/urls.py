from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from usuario.router import router as usuario_router


from django.contrib import admin
from django.urls import path, include
from core.views import FilaViewSet, ModalidadeViewSet, ServicoViewSet, EloViewSet, StatusViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r"fila", FilaViewSet)
router.register(r"modalidade", ModalidadeViewSet)
router.register(r"servico", ServicoViewSet)
router.register(r"elo", EloViewSet)
router.register(r"elo", StatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
