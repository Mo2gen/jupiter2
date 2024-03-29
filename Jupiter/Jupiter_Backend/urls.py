from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'Forecast', views.ForecastHourViewSet)
router.register(r'Forecast_Request', views.ForecastRequestViewSet)

urlpatterns = [
    path('', include(router.urls))
]