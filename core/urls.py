from .views import IndexView, DadosJSONView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
]